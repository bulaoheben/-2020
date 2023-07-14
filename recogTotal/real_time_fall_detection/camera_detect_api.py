import datetime
import os
import threading
import time
import cv2
import torch
import torch.nn as nn
import math
from collections import deque
from ultralytics import YOLO
from app import static_path, db
from PIL import Image

from app.mod_event.models import EventInfo


class fc(nn.Sequential):
    def __init__(self, ):
        super(fc, self).__init__()

        # self.fc1 = nn.Linear(3, 64)  # MLP(1), MLP(2), MLP(7), MLP(8)
        self.fc1 = nn.Linear(4, 64)  # MLP(5), MLP(6), MLP(9)
        self.act1 = nn.ReLU()

        self.fc2 = nn.Linear(64, 64)
        self.act2 = nn.ReLU()

        self.fc3 = nn.Linear(64, 2)

    def forward(self, out):
        out = self.fc1(out)
        out = self.act1(out)

        out = self.fc2(out)
        out = self.act2(out)

        out = self.fc3(out)

        return out


class FallDetection:
    def __init__(self, model_fall_path, model_yolo_path, list_length=2, thresh_con=0.0, thresh_con_p=0.4):
        # 时间窗口初始化
        self.windows = {}
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.list_length = list_length
        self.thresh_con = thresh_con
        self.thresh_con_p = thresh_con_p

        # Load the fall detection model
        self.model_fall = torch.load(model_fall_path)
        self.model_fall.to(self.device)
        self.model_fall.eval()

        # Load the YOLO model
        self.model_yolo = YOLO(model_yolo_path)
        self.model_yolo.classes = [0]
        self.model_yolo.to(self.device)

        # Initialize deque and other variables
        self.deq = deque(maxlen=self.list_length)
        self.frames_4 = deque(maxlen=self.list_length)
        if self.list_length == 2:
            self.dew = [[], []]
        else:
            self.dew = []

    def remove_window(self, event_id):
        del self.windows[event_id]

    def fallen(self, start_point, end_point, w, h):
        wb = end_point[0] - start_point[0]
        hb = end_point[1] - start_point[1]

        AR = wb / hb
        NW = wb / w
        NH = hb / h
        NB = 1 - (end_point[1] / h)
        DIAG = math.sqrt(math.pow(wb, 2) + math.pow(hb, 2)) / math.sqrt(math.pow(h, 2) + math.pow(w, 2))
        AREA = (wb * hb) / (h * w)

        # Data for the MLP model
        data = [AR, NW, NB, DIAG]

        data_tensor = torch.FloatTensor(data).to(self.device)
        scores = self.model_fall(data_tensor)
        s = nn.Softmax()
        conf = (s(scores).max().cpu().detach().numpy())
        _, predict = scores.max(0)

        return predict, conf, AR, NW, NH, DIAG

    def process_frame(self, frame):
        pred = 1
        con = 0.0
        cv2.putText(frame, text="Live Video", org=(10, 450), fontFace=cv2.FONT_HERSHEY_TRIPLEX,
                    fontScale=1, color=(0, 0, 255), thickness=2)

        im_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w = im_rgb.shape[:2]

        results = self.model_yolo(im_rgb)
        xy = results[0].boxes.xyxy
        clss = results[0].boxes.cls
        conf = results[0].boxes.conf

        flag_0 = False
        for cl in clss:
            if cl == 0:
                flag_0 = True

        xy_np = xy.cpu().detach().numpy()
        clss_np = clss.cpu().detach().numpy()
        conf_np = conf.cpu().detach().numpy()

        start_point = ()
        end_point = ()

        if len(xy_np) > 0 and flag_0:
            for j in range(len(xy_np)):
                if clss_np[j] == 0 and conf_np[j] > self.thresh_con_p:
                    start_point = (int(xy_np[j][0]), int(xy_np[j][1]))
                    end_point = (int(xy_np[j][2]), int(xy_np[j][3]))

                    pre_frame = frame.copy()
                    pre_box = (int(xy_np[j][0]), int(xy_np[j][1]),
                               abs(int(xy_np[j][2]) - int(xy_np[j][0])), abs(int(xy_np[j][3]) - int(xy_np[j][1])))

                    pred, con, ar, nw, nh, dia = self.fallen(start_point, end_point, w, h)

                    xmin = start_point[0]
                    ymin = start_point[1]
                    xmax = end_point[0]
                    ymax = end_point[1]

                    if pred == 0 and con > self.thresh_con:
                        cv2.rectangle(frame, start_point, end_point, color=(0, 0, 255), thickness=2)
                    else:
                        cv2.rectangle(frame, start_point, end_point, color=(0, 255, 0), thickness=2)
        else:
            pass

        if len(start_point) > 0 and con > self.thresh_con:
            if start_point[0] != end_point[0] and start_point[1] != end_point[1]:
                self.deq.append([pred, con, ar, nw, nh, dia])
                self.frames_4.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        else:
            pass

        if len(self.deq) == self.list_length:
            flag = False

            if self.list_length == 2:
                if self.deq[0][0] == 1 and self.deq[1][0] == 0 and self.deq[1][1] > self.thresh_con:
                    flag = True
                else:
                    flag = False

            flag_nextPrev_deq = False

            if len(self.dew[0]) == 6 and flag:
                for item in range(2, 6, 1):
                    if self.dew[0][item] != self.deq[0][item]:
                        flag_nextPrev_deq = True

            if flag_nextPrev_deq and flag:
                fall_flag = True
                fall_flag2 = True
                # count_of_falls += 1

        if self.list_length == 2:
            self.dew = [[], []]
        else:
            pass
        for le in range(len(self.deq)):
            for le2 in range(len(self.deq[le])):
                self.dew[le].append(self.deq[le][le2])

        # 如果检测到跌倒事件
        if pred == 0 and con > self.thresh_con:
            if "3" not in self.windows:
                # 开启新的时间窗口，保存截图，插入数据库
                window_start_time = datetime.datetime.now()
                window_end_time = window_start_time + datetime.timedelta(seconds=5)  # 设置时间窗口的长度为5秒
                self.windows["3"] = (window_start_time, window_end_time)
                # 设置定时器，在时间窗口结束后删除时间窗口
                timer = threading.Timer(5, self.remove_window, args=["3"])
                timer.start()

                now_datetime = time.strftime("%Y-%m-%d %H:%M:%S",
                                             time.localtime(time.time()))  # 当前系统时间
                now_datetime2 = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))  # 当前系统时间

                # 保存截图为图片文件
                filename = static_path + f'event\\event_3_{now_datetime2}.jpg'  # 根据需要构建文件名
                img = Image.fromarray(frame)
                img.save(filename)

                # 检查图片是否已经成功保存
                if os.path.exists(filename):
                    # 插入数据库中
                    event = EventInfo(event_type=3,
                                      event_date=now_datetime,
                                      event_location=None,
                                      event_desc=f"{now_datetime}检测到有人摔倒",
                                      oldperson_id=None,
                                      pic_url=f'event\\event_3_{now_datetime2}.jpg')
                    db.session.add(event)
                    db.session.commit()

        return frame

# Example usage
# fall_detection = FallDetection(
#     model_fall_path=fall_path + 'fall_no-fall_models/deep_learning_models/MLP(9).pt',
#     model_yolo_path=fall_path + 'yolov8/train13_n_no_rotated/weights/best.pt',
#     list_length=2,
#     thresh_con=0.0,
#     thresh_con_p=0.4
# )

# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#
#     if not ret:
#         break
#
#     processed_frame = fall_detection.process_frame(frame)
#
#     cv2.imshow('Processed Frame', processed_frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
