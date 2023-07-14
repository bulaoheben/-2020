import base64
import os
import numpy as np
from flask import Response, Blueprint, request, send_file, jsonify
import cv2
import recogTotal.facenet_retinaface_pytorch.api.recog_emotion_api as emotion_api
import recogTotal.religion_forbiden.fence_forbiden as fence_api
from app import static_path
from recogTotal.real_time_fall_detection import fall_path
from recogTotal.real_time_fall_detection.camera_detect_api import FallDetection, fc

app_video = Blueprint('video', __name__)
camera = cv2.VideoCapture(0)  # 0表示默认的摄像头


# 传输区域入侵检测的视频流
def generate_frames_forbidden():
    # 初始化
    emotion_func = fence_api.fenceForbiden()
    while True:
        # 读取摄像头视频帧
        success, frame = camera.read()
        if not success:
            break
        else:
            processed_frame = emotion_func.fenceForbidenAPI(ret=success, frame=frame)

            # 将处理后的帧转换为图片格式
            ret, buffer = cv2.imencode('.jpg', processed_frame)
            frame_bytes = buffer.tobytes()

            # 返回处理后的图片给前端
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    camera.release()  # 释放摄像头资源


# 表情识别和陌生人检测和义工交互
def generate_frames():
    emotion_func = emotion_api.recog_emotion_activity()
    while True:
        # 读取摄像头视频帧
        success, frame = camera.read()
        if not success:
            break
        else:
            processed_frame = emotion_func.recog_emotion_activity_api(frame=frame)

            # 将处理后的帧转换为图片格式
            ret, buffer = cv2.imencode('.jpg', processed_frame)
            frame_bytes = buffer.tobytes()

            # 返回处理后的图片给前端
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    camera.release()  # 释放摄像头资源


# 传输与人脸相关的算法处理后的视频流
@app_video.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


# 区域入侵检测接口
@app_video.route('/video_fence_forbidden')
def video_fence_forbidden():
    return Response(generate_frames_forbidden(), mimetype='multipart/x-mixed-replace; boundary=frame')


# 跌倒检测处理
def generate_frames_fall():
    fall_func = FallDetection(model_fall_path=fall_path + 'fall_no-fall_models/deep_learning_models/MLP(9).pt',
                              model_yolo_path=fall_path + 'yolov8/train13_n_no_rotated/weights/best.pt',
                              list_length=2,
                              thresh_con=0.0,
                              thresh_con_p=0.4)
    while True:
        # 读取摄像头视频帧
        success, frame = camera.read()
        if not success:
            break
        else:
            processed_frame = fall_func.process_frame(frame=frame)

            # 将处理后的帧转换为图片格式
            ret, buffer = cv2.imencode('.jpg', processed_frame)
            frame_bytes = buffer.tobytes()

            # 返回处理后的图片给前端
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    camera.release()  # 释放摄像头资源


@app_video.route('/video_fall')
def fall():
    return Response(generate_frames_fall(), mimetype='multipart/x-mixed-replace; boundary=frame')


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
