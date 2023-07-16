from flask import Blueprint
from app import app
import recogTotal.chat.chatRobot as chat

app_chat = Blueprint('chat', __name__)


# 开始说话
@app.route('/startChat', methods=['POST'])
def startChat():
    response = {}
    chat.startSaveVoice()
    response['code'] = 200
    response['message'] = 'true'
    return response


# 结束说话
@app.route('/finishChat')
def finishChat():
    response = {}
    reply = chat.deal()
    response['code'] = 200
    response['user'] = reply['user']
    response['robot'] = reply['robot']
    return response
