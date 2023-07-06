from app import app
from flask import render_template, Response, Blueprint
import cv2

app_video = Blueprint('video', __name__)
camera = cv2.VideoCapture(0)  # 0表示默认的摄像头


def generate_frames():
    while True:
        # 读取摄像头视频帧
        success, frame = camera.read()
        if not success:
            break
        else:
            # 在这里可以对视频帧进行算法端的处理
            # processed_frame = algorithm_process(frame)

            # 将处理后的帧转换为图片格式
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # 返回处理后的图片给前端
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
