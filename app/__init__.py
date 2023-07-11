import os

from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Zjq123789@bj-cynosdbmysql-grp-qzs817me.sql.tencentcdb.com:27204' \
                                        '/xiaoxueqi'
db = SQLAlchemy(app)  # 初始化数据库
socketio = SocketIO(app, async_mode='threading')

# 静态资源的目录路径
static_path = os.path.dirname(os.path.abspath(__file__)) + "\\static\\"
