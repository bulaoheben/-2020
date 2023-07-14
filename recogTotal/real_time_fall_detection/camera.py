import cv2
import torch
import torch.nn as nn
import math
import numpy as np
import pandas as pd
from collections import deque
import matplotlib.pyplot as plt
from ultralytics import YOLO

"""
# Class for the architect of the MLPs, fc1 input is changed according to the input (3 or 4).
"""


class fc(nn.Sequential):
    def __init__(self, ):
        super(fc, self).__init__()

        # self.fc1 = nn.Linear(3, 64)  # MLP(1), MLP(2), MLP(7), MLP(8)
        self.fc1 = nn.Linear(4,64) # MLP(5), MLP(6), MLP(9)
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


"""
# The fallen def gets the bounding box variables (start_point, end_point), 
# the width and height of the frame (w, h), and the chosen DL model MLP (model_f).
# The inindependent variables are extracted (feature extraction) and are loaded to the model, 
# finally the prediction is returned along with confidence and 4 of the features.
# These features are used later for a check.
"""


def fallen(start_point, end_point, w, h, model_f):
    wb = end_point[0] - start_point[0]
    hb = end_point[1] - start_point[1]

    AR = wb / hb
    NW = wb / w
    NH = hb / h
    NB = 1 - (end_point[1] / h)
    DIAG = math.sqrt(math.pow(wb, 2) + math.pow(hb, 2)) / math.sqrt(math.pow(h, 2) + math.pow(w, 2))
    AREA = (wb * hb) / (h * w)

    '''# The appropriate variables should be choosen for the corresponding MLP.'''
    # data = [AR, NW, NB] # MLP(1), MLP(7)
    # data = [AR, NH, NB]  # MLP(2), MLP(8)
    # data = [AR, NW, NB, AREA] # MLP(5)
    data = [AR, NW, NB, DIAG] # MLP(6), MLP(9)

    data_tensor = torch.FloatTensor(data).to(device)
    scores = model_f(data_tensor)
    s = nn.Softmax()
    conf = (s(scores).max().cpu().detach().numpy())
    _, predict = scores.max(0)

    return predict, conf, AR, NW, NH, DIAG


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model_fall = torch.load('fall_no-fall_models/deep_learning_models/MLP(9).pt')
model_fall.to(device)
model_fall.eval()
'''# Give the path to the YOLO (.pt) model'''
model = YOLO('yolov8/train13_n_no_rotated/weights/best.pt')

model.classes = [0]
model.to(device)
# video_path = 'path to the folder where all the videos of target dataset are.'
# df = pd.read_csv('path to the csv file that contains the labels and the names of the corresponding videos (labels.csv)')

# videos = df.name[:].to_list()
# true_fall = df.label[:].to_list()
y_pred = []

frame_step = 17

list_length = 2
thresh_con = 0.0
thresh_con_p = 0.4

deq = deque(maxlen=list_length)
frames_4 = deque(maxlen=list_length)

if list_length == 2:
    dew = [[], []]
else:
    dew = []

pred_fall = []
total_of_falls = []

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.putText(frame, text="Live Video", org=(10, 450), fontFace=cv2.FONT_HERSHEY_TRIPLEX,
                fontScale=1, color=(0, 0, 255), thickness=2)

    im_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    h, w = im_rgb.shape[:2]

    results = model(im_rgb)

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
            if clss_np[j] == 0 and conf_np[j] > thresh_con_p:
                start_point = (int(xy_np[j][0]), int(xy_np[j][1]))
                end_point = (int(xy_np[j][2]), int(xy_np[j][3]))

                pre_frame = frame.copy()
                pre_box = (int(xy_np[j][0]), int(xy_np[j][1]),
                           abs(int(xy_np[j][2]) - int(xy_np[j][0])), abs(int(xy_np[j][3]) - int(xy_np[j][1])))

                pred, con, ar, nw, nh, dia = fallen(start_point, end_point, w, h, model_fall)
                xmin = start_point[0]
                ymin = start_point[1]
                xmax = end_point[0]
                ymax = end_point[1]

                if pred == 0 and con > thresh_con:
                    cv2.rectangle(frame, start_point, end_point, color=(0, 0, 255), thickness=2)
                else:
                    cv2.rectangle(frame, start_point, end_point, color=(0, 255, 0), thickness=2)
    else:
        pass

    if len(start_point) > 0 and con > thresh_con:
        if start_point[0] != end_point[0] and start_point[1] != end_point[1]:
            deq.append([pred, con, ar, nw, nh, dia])
            frames_4.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    else:
        pass

    if len(deq) == list_length:
        flag = False

        if list_length == 2:
            if deq[0][0] == 1 and deq[1][0] == 0 and deq[1][1] > thresh_con:
                flag = True
            else:
                flag = False

        flag_nextPrev_deq = False

        if len(dew[0]) == 6 and flag:
            for item in range(2, 6, 1):
                if dew[0][item] != deq[0][item]:
                    flag_nextPrev_deq = True

        if flag_nextPrev_deq and flag:
            fall_flag = True
            fall_flag2 = True
            # count_of_falls += 1

    if list_length == 2:
        dew = [[], []]
    else:
        pass
    for le in range(len(deq)):
        for le2 in range(len(deq[le])):
            dew[le].append(deq[le][le2])

    cv2.imshow('Processed Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
