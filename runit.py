from app import app, socketio
from app.mod_auth.employeeController import app03
from app.mod_auth.forms import app02
from app.views import app01

# 注册路由
app.register_blueprint(app01, url_prefix='/app01')
app.register_blueprint(app02, url_prefix='/app02')
app.register_blueprint(app03, url_prefix='/app03')


if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', debug=True, port=5000, allow_unsafe_werkzeug=True)
