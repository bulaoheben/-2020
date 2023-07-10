from app import app, socketio
from app.mod_auth.employeeController import app03
from app.mod_auth.forms import app02
from app.mod_event.controllers import event
from app.mod_oldperson.controllers import oldperson
from app.mod_video.video import app_video
from app.mod_volunteer.controllers import app_volunteer

# 注册路由
app.register_blueprint(app02, url_prefix='/app02')
app.register_blueprint(app03, url_prefix='/app03')
app.register_blueprint(app_volunteer, url_prefix='/volunteer')
app.register_blueprint(app_video, url_prefix='/video')
app.register_blueprint(oldperson, url_prefix='/oldperson')
app.register_blueprint(event, url_prefix='/event')

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', debug=True, port=5000, allow_unsafe_werkzeug=True)
