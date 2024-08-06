# exts.py：插件管理

# 1.导入第三方插件
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_restful import Api

# 2.初始化
db = SQLAlchemy()
migrate = Migrate()
# 初始化flask-caching
cache = Cache(config={
    # 使用简单的内存缓存
    'CACHE_TYPE': 'simple',
    # 设置缓存的默认过期时间为60秒
    'CACHE_DEFAULT_TIMEOUT': 60
})
api = Api()


# 3.和app对象绑定
def init_exts(app):
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    api.init_app(app)
