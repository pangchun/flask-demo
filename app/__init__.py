# __init__.py: 初始化，创建Flask应用
from flask import Flask

from .exts import init_exts
from app.views.views import main_bp
from .urls import *


def create_app():
    app = Flask(__name__)

    # 注册蓝图
    app.register_blueprint(blueprint=main_bp)

    # 设置session key
    app.config['SECRET_KEY'] = 'your-secret-key-here'

    # 配置mysql数据库连接
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/flask_demo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 初始化插件
    init_exts(app)

    # 注册钩子函数【请求前执行】
    @app.before_request
    def before_request2():
        print('before_request')
        # 打印当前请求的ip地址
        print('ip地址：' + request.remote_addr)
        # 打印当前请求的完整路径
        print('请求url：' + request.url)
        # 打印当前请求的路径，不包含ip地址和路径参数
        print('请求路径：' + request.path)

        # 定义g对象【可以在进入请求后引用】
        g.star = '杰伦'

        # 使用cache缓存当前请求的ip地址和请求时间，和请求路径
        ip = request.remote_addr
        if cache.get(ip):
            return '访问过于频繁，请稍后再试'
        else:
            cache.set(ip, request.remote_addr, timeout=1)

    return app
