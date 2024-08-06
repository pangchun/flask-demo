from flask import Blueprint, g

from app.exts import cache

# 导入模型【如果不导入，模型相关代码不会执行，数据迁移会找不到相关的数据表】

main_bp = Blueprint('main', __name__)


# 视图
@main_bp.route('/home', methods=['GET'])
@cache.cached(timeout=20)
def home():
    print(g.star)
    return 'hello world'
