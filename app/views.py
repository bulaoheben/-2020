from app import app
from flask import render_template, Blueprint
import secrets

app01 = Blueprint('index', __name__)


def generate_csrf_token():
    token = secrets.token_hex(16)
    return token


@app.route('/login.html')
@app.route('/')
def index():
    csrf_token = generate_csrf_token()  # 自行实现生成 CSRF 令牌的逻辑
    return render_template('login.html', csrf_token=csrf_token)
