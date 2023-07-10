import os

from flask import Response, Blueprint, request, send_file
import cv2
from the_old_fall.api.stranger_facial_expression import strangerFacialExpression

app_video = Blueprint('video', __name__)
camera = cv2.VideoCapture(0)  # 0表示默认的摄像头


def generate_frames():
    buf = strangerFacialExpression()
    counter = 0
    while True:
        # 读取摄像头视频帧
        success, frame = camera.read()
        if not success:
            break
        else:
            counter += 1
            # 获得事件id
            (event_id, processed_frame, flag) = buf.strangerFacialExpressionAPI(success, frame, counter)
            if flag:
                break

            # 若检测到事件，则插入数据库

            # 将处理后的帧转换为图片格式
            ret, buffer = cv2.imencode('.jpg', processed_frame)
            frame_bytes = buffer.tobytes()

            # 返回处理后的图片给前端
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    camera.release()  # 释放摄像头资源


@app_video.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app_video.route('/get_pic', methods=['POST'])
# def get_image():
#     # 从前端请求中获取图片路径
#     image_path = request.json.get('image_path')
#
#     # 构建完整的图片路径
#     full_image_path = os.path.join('path/to/images', image_path)
#
#     # 检查图片是否存在
#     if os.path.exists(full_image_path):
#         # 设置正确的MIME类型和Content-Disposition头部信息
#         return send_file(full_image_path, mimetype='image/jpeg', as_attachment=False)
#     else:
#         # 图片不存在时返回错误信息
#         return 'Image not found', 404
