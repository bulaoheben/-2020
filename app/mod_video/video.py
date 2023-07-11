import base64
import os
import numpy as np
from flask import Response, Blueprint, request, send_file, jsonify
import cv2
import datetime

from app import static_path

app_video = Blueprint('video', __name__)
camera = cv2.VideoCapture(0)  # 0表示默认的摄像头
# 在生成帧的循环中定义时间窗口的相关变量
windows = {}  # 用字典来存储不同事件ID对应的时间窗口


def strangerFacialExpressionAPI(success, frame, counter):
    return


def generate_frames():
    counter = 0
    while True:
        # 读取摄像头视频帧
        success, frame = camera.read()
        if not success:
            break
        else:
            flag = False
            counter += 1
            # 获得事件id，处理后的图像processed_frame，是否出现故障flag，事件对应的描述description
            (event_id, processed_frame, flag, description) = strangerFacialExpressionAPI(success, frame, counter)
            if flag:
                break

            # 判断是否需要保存截图
            if event_id in [0, 1, 2, 3, 4]:
                if event_id not in windows:
                    # 开启新的时间窗口，保存截图
                    window_start_time = datetime.datetime.now()
                    window_end_time = window_start_time + datetime.timedelta(seconds=5)  # 设置时间窗口的长度为5秒
                    windows[event_id] = (window_start_time, window_end_time)
                    # 保存截图为图片文件
                    filename = f'event_{event_id}_{counter}.jpg'  # 根据需要构建文件名
                    cv2.imwrite(filename, processed_frame)  # 保存截图为图片文件

            # 将处理后的帧转换为图片格式
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            # 返回处理后的图片给前端
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

            # 检查时间窗口是否结束
            for event_id, (window_start_time, window_end_time) in list(windows.items()):
                if datetime.datetime.now() > window_end_time:
                    # 删除时间窗口
                    del windows[event_id]

    camera.release()  # 释放摄像头资源


# 传输处理后的视频流
@app_video.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


# 传入事件图片名称，获取图片
@app_video.route('/get_pic', methods=['POST'])
def get_image():
    # 从前端请求中获取图片路径
    image_path = request.json.get('image_name')

    # 构建完整的图片路径
    full_image_path = os.path.join(static_path, image_path)

    # 检查图片是否存在
    if os.path.exists(full_image_path):
        # 设置正确的MIME类型和Content-Disposition头部信息
        return send_file(full_image_path, mimetype='image/jpg', as_attachment=False)
    else:
        # 图片不存在时返回错误信息
        response = {"code": "23", "message": "Image not found."}
        return response


# 调用摄像头信息录入人脸信息
@app_video.route('/collect_face', methods=['POST'])
def collect_face():
    # 从前端获取正在收集信息的对象名字和图像数据
    name = request.json.get('name')
    image_data_url = request.json.get('imageDataUrl')

    # 将图像数据转换为OpenCV图像
    image_data = base64.b64decode(image_data_url.split(',')[1])
    np_arr = np.frombuffer(image_data, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # 将拍照得到的照片存在本地
    file_name = static_path + f'face_collection\\{name}_1.jpg'
    cv2.imwrite(file_name, frame)

    # 检查文件是否存在
    if os.path.exists(file_name):
        response = {"code": "200", "message": "Image saved successfully."}
    else:
        response = {"code": "23", "message": "Failed to save image."}

    return jsonify(response)
