# 基于flask搭建后端学习项目

[Welcome to Flask — Flask Documentation (3.0.x) (palletsprojects.com)](https://flask.palletsprojects.com/en/3.0.x/)

目前正在学习python基础，打算先用flask搭建一个基础的后端框架，并连接mysql数据库，完成增删改查等基础接口的编写，了解python后端的基本写法。

> 注意：这个项目的demo已经放在github中，可以下载后作为脚手架使用



## flask简介



### 1、python后端主流框架

python后端主要的两个框架：

1. flask：轻量级
2. django：重量级

> 区别：
>
> 1. 其实是先有的django，flask是模仿的django实现的轻量级框架。
> 2. flask只提供了 Web 应用开发的核心功能，比如路由、请求处理、模板渲染等，其它的扩展系统自行添加。



### 2、flask mtv模式

flask是一个基于mvc模式的web后端框架。

mvc：

1. m：modle数据模型
2. v：view界面
3. c：controller控制器

mtv：

1. m：modle模型（数据）
2. t：template模板（界面）
3. views视图（控制器）

> 不难发现，mvc和mtv本质上是一样的模式。



### 3、模板引擎

flask依赖jinja模板引擎，类似于java中的jsp。

> [Jinja](https://palletsprojects.com/p/jinja/) is a template language that renders the pages your application serves.



## 虚拟环境创建



### 1、虚拟环境是什么

虚拟环境：python项目的虚拟环境是一个独立的目录，包含了完整的python解释器，以及一套独立的依赖库；当有多个python项目时，每个项目使用不用的python版本、有不同的依赖软件包，我们可以创建多个虚拟环境来分别对应不同的python项目。



### 2、安装anaconda

[超详细版Anaconda的安装及使用conda创建、运行虚拟环境以及使用镜像源_anaconda镜像源-CSDN博客](https://blog.csdn.net/weixin_73800108/article/details/137296446)

可以通过python自身的venv来管理虚拟环境、或者使用第三方工具来管理虚拟环境，常用的虚拟环境创建工具主要有如下几个venv、pipenv、poetry、conda。

我打算使用conda来管理虚拟环境，因此需要先安装anaconda。

> Anaconda 是一个大型的环境管理系统，支持 Python/R 在内的多种语言。安装 Anaconda 或 Miniconda（精简版） 之后就能使用 conda 命令来创建和管理 Python 环境。
>
> 下载地址：[Download Now | Anaconda](https://www.anaconda.com/download/success)

安装完成后，在anaconda页面中打开控制台，输入以下命令，检查是否安装成功：

```bash
(base) C:\Users\chun>conda --version
conda 24.5.0
```



### 3、虚拟环境创建

可以在页面内手动创建：

![image-20240723182519237](assets/image-20240723182519237.png)

也可以使用命令行创建：

```bash
# 创建一个虚拟环境
(base) C:\Users\chun>conda create -n my_env_2 python=3.12.4

# 激活/切换一个虚拟环境
(base) C:\Users\chun>conda activate my_env_2
(my_env_2) C:\Users\chun>

# 查看虚拟环境列表
(base) C:\Users\chun>conda env list
# conda environments:
#
base                  *  C:\env\anaconda3
my_env_1                 C:\env\anaconda3\envs\my_env_1
my_env_2                 C:\env\anaconda3\envs\my_env_2

# 删除一个虚拟环境
(base) C:\Users\chun>conda env remove -n  my_env_2

# 退出虚拟环境
C:\Users\chun>deactivate
DeprecationWarning: 'deactivate' is deprecated. Use 'conda deactivate'.

# 查看当前使用的虚拟环境
(base) C:\Users\chun>conda info

     active environment : base
    active env location : C:\env\anaconda3
            shell level : 2
       user config file : C:\Users\chun\.condarc
 populated config files : C:\Users\chun\.condarc
          conda version : 24.5.0
    conda-build version : 24.5.1
         python version : 3.12.4.final.0
                 solver : libmamba (default)
       virtual packages : __archspec=1=x86_64_v4
                          __conda=24.5.0=0
                          __win=0=0
       base environment : C:\env\anaconda3  (writable)
      conda av data dir : C:\env\anaconda3\etc\conda
  conda av metadata url : None
           channel URLs : https://repo.anaconda.com/pkgs/main/win-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/win-64
                          https://repo.anaconda.com/pkgs/r/noarch
                          https://repo.anaconda.com/pkgs/msys2/win-64
                          https://repo.anaconda.com/pkgs/msys2/noarch
          package cache : C:\env\anaconda3\pkgs
       envs directories : C:\env\anaconda3\envs
                          C:\Users\chun\.conda\envs
                          C:\Users\chun\AppData\Local\conda\conda\envs
               platform : win-64
             user-agent : conda/24.5.0 requests/2.32.2 CPython/3.12.4 Windows/11 Windows/10.0.22631 solver/libmamba conda-libmamba-solver/24.1.0 libmambapy/1.5.8 aau/0.4.4 c/. s/. e/.
          administrator : True
             netrc file : None
           offline mode : False
```

创建虚拟环境后，可以使用命令查看虚拟环境中有哪些包：

```bash
(my_env_1) C:\Users\chun>pip list
Package    Version
---------- -------
pip        24.0
setuptools 69.5.1
wheel      0.43.0
```



## 创建flask应用



### 1、创建虚拟环境

```bash
# 创建虚拟环境
(base) C:\Users\chun>conda create -n flask_env python=3.12.4

# 切换虚拟环境
(base) C:\Users\chun>conda activate flask_env

# 查看虚拟环境中的已有包
(flask_env) C:\Users\chun>pip list
Package    Version
---------- -------
pip        24.0
setuptools 69.5.1
wheel      0.43.0

# 安装flask
(flask_env) C:\Users\chun>pip install Flask

# 查看依赖包
(flask_env) C:\Users\chun>pip list
Package      Version
------------ -------
blinker      1.8.2
click        8.1.7
colorama     0.4.6
Flask        3.0.3
itsdangerous 2.2.0
Jinja2       3.1.4
MarkupSafe   2.1.5
pip          24.0
setuptools   69.5.1
Werkzeug     3.0.3
wheel        0.43.0
```



### 2、使用PyCharm创建一个flask项目

![image-20240723192701648](assets/image-20240723192701648.png)

启动项目：

![image-20240723193319508](assets/image-20240723193319508.png)

前端访问：http://127.0.0.1:5000 就能在页面上看到一句`Hello World!`。

设置调试模式：

```python
if __name__ == '__main__':
    # debug开启调试模型，修改代码会自动重启
    app.run(debug=True, port=8888, host='0.0.0.0')
```

如果修改代码页面刷新后未发生改变，需要如下设置编辑器：

![image-20240723204125497](assets/image-20240723204125497.png)



### 3、接口返回不同的类型

```python
from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# 返回html模板
@app.route('/index')
def index():
    return render_template('index.html', name='zhangsan')


# 返回json，序列化
@app.route('/json')
def json():
    return jsonify({'name': 'zhangsan', 'age': 18})


if __name__ == '__main__':
    # debug开启调试模型，修改代码会自动重启
    app.run(debug=True, port=8888, host='0.0.0.0')
```



### 4、项目目录拆分

如下图，在项目根目录上右键创建一个python package并命名为app，创建后会自动生成一个`__init__.py`文件，这是我们flask应用的入口文件。（注意：以下划线开头的文件一般都是系统自动创建的，不是我们手动创建的）

![image-20240724114327528](assets/image-20240724114327528.png)

在idea的控制台输入`tree /f`打印当前项目目录结构：

```
C:.
│  app.py
│
├─.idea
│  │  .gitignore
│  │  flask-demo.iml
│  │  misc.xml
│  │  modules.xml
│  │  workspace.xml
│  │
│  └─inspectionProfiles
│          profiles_settings.xml
│
├─app
│  │  models.py
│  │  views.py
│  │  __init__.py
│  │
│  ├─static
│  ├─templates
│  │      index.html
│  │
│  └─__pycache__
│          __init__.cpython-312.pyc
│
└─__pycache__
        app.cpython-312.pyc
```

> 文件说明：
>
> 1. models.py：数据模型文件，用于与数据库交互
> 2. views.py：视图层，提供接口与逻辑交互
> 3. `__init__.py`：应用入口文件，只初始化一次



### 5、路由参数

支持以下几种类型：string、int、float、path、uuid、any

```python
import uuid

from flask import Blueprint

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return 'this is the main page'


# 路由参数：string(默认string，可省略)
@main_bp.route('/string/<username>')
def get_string(username):
    print(username)
    return username


# 路由参数：int
@main_bp.route('/int/<int:age>')
def get_int(age):
    print(type(age))
    return str(age)


# 路由参数：float
@main_bp.route('/float/<float:money>')
def get_float(money):
    print(type(money))
    return str(money)


# 路由参数：path
@main_bp.route('/path/<path:name>')
def get_path(name):
    print(type(name))
    return str(name)


# 路由参数：uuid (47c91f6b-4988-11ef-821e-4e50dd3d93aa)
@main_bp.route('/uuid/<uuid:id>')
def get_uuid(id):
    print(type(id))
    return str(id)


# 路由参数：uuid
@main_bp.route('/uuid')
def get_uuid2():
    return str(uuid.uuid1())


# 路由参数：any
@main_bp.route('/any/<any(apple,orange,banana):fruit>')
def get_any(fruit):
    print(type(fruit))
    return str(fruit)
```



### 6、请求参数

```python
from flask import Blueprint, request

main_bp = Blueprint('main', __name__)


@main_bp.route('/api', methods=['POST', 'GET'])
def index():
    # 请求方法
    print(request.method)

    # 从url中获取请求参数
    # print(request.args)
    # print(request.args['name'], request.args['id'])
    # print(request.args.get('name'))
    # print(request.args.getlist('name'))

    # 从form中获取请求参数
    # print(request.form.get('name'))

    # 从json中获取请求参数
    # print(request.json)

    # 从cookie中获取请求参数
    print(request.cookies)

    print(request.path)
    print(request.url)
    print(request.base_url)
    print(request.host_url)
    # 远程地址
    print(request.remote_addr)
    # 请求头
    print(request.headers)
    # 上传文件内容
    print(request.files)
    # 用户代理，包括浏览器和操作系统信息
    print(request.user_agent)

    return 'ok'
```



### 7、响应参数

```python
from flask import Blueprint, request, render_template, jsonify, make_response, Response

main_bp = Blueprint('main', __name__)


@main_bp.route('/api', methods=['POST', 'GET'])
def index():
    pass

    # 直接返回字符串
    # return 'ok'

    # 返回json数据
    # data = {
    #     'code': 200,
    #     'msg': 'ok',
    #     'data': {
    #         'name': 'zhangsan',
    #         'age': 18
    #     }
    # }
    # return jsonify(data)

    # 返回模板渲染
    # return render_template('index.html')

    # 返回自定义响应对象
    # html = render_template('index.html')
    # return make_response(html, 200)

    # 返回Response对象
    html = render_template('index.html')
    return Response(html)
```



### 8、重定向

```python
from flask import Blueprint, request, render_template, jsonify, make_response, Response, redirect, url_for

main_bp = Blueprint('main', __name__)


@main_bp.route('/api', methods=['POST', 'GET'])
def index():
    return 'api'


@main_bp.route('/test', methods=['POST', 'GET'])
def index2():
    # 重定向到系统内页面
    # return redirect('/api')

    # 重定向到系统外页面
    # return redirect('https://www.baidu.com/')

    # 重定向url_for
    ret = url_for('main.index')
    print(ret)
    return redirect(ret)
```



### 9、会话技术：cookie

cookie有如下特点：

1. cookie是服务端创建和管理的
2. 可以设置过期时间
3. 浏览器关闭后自动清空



下面通过演示登录注册来展示cookie的使用：

```python
import datetime

from flask import Blueprint, request, render_template, jsonify, make_response, Response, redirect, url_for

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
@main_bp.route('/home')
def home():
    # 获取cookie
    username = request.cookies.get('username')
    return render_template('home.html', username=username)


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        pass
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin123':
            resp = redirect('/home')
            # 设置cookie 【默认关闭浏览器，cookie就失效了】
            resp.set_cookie('username', username, max_age=3600)
            resp.set_cookie('password', password, expires=datetime.datetime(2024, 12, 31, 23, 59, 59))
            return resp
        else:
            return '用户名或密码错误'


@main_bp.route('/logout')
def logout():
    resp = redirect('/home')
    # 删除cookie
    resp.delete_cookie('username')
    resp.delete_cookie('password')
    return resp
```



### 10、会话技术：session

session是服务端的会话技术，依赖于cookie，数据存储在服务器的内存中，也是以键值对的形式存储。

以下将改写上面cookie，通过session的方式完成登录注销功能：

```python
import datetime

from flask import Blueprint, request, render_template, jsonify, make_response, Response, redirect, url_for, session

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
@main_bp.route('/home')
def home():
    # 获取cookie
    username = session.get('username')
    return render_template('home.html', username=username)


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        pass
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin123':
            resp = redirect('/home')
            # 设置session
            session['username'] = username
            session['password'] = password
            return resp
        else:
            return '用户名或密码错误'


@main_bp.route('/logout')
def logout():
    resp = redirect('/home')
    # 删除session
    session.pop('username')
    session.pop('password')
    return resp
```



### 11、模板语言

这个模板语言其实是类似于jsp的东西，跳过。



## 数据模型



### 1、orm框架

flask默认并没有提供任何数据库操作的api，flask可以使用原生sql语句，但是不方便。

flask可以通过orm框架去操作数据库，类似于java中的mybatis。

1. flask使用python自带的orm：sqlAlchemy
2. 针对flask的支持，提供了flask-sqlalchemy插件
3. 安装方式：`pip install flask-sqlalchemy`



### 2、安装flask-sqlalchemy

```bash
# 安装Flask-SQLAlchemy以及用于连接MySQL的适配器PyMySQL

# 安装完成后提示：Successfully installed Flask-SQLAlchemy-3.1.1 PyMySQL-1.1.1 greenlet-3.0.3 sqlalchemy-2.0.31 typing-extensions-4.12.2

# 这些包好像是从国外网站下载的，需要挂代理，没有代理的需要找一下有没有国内镜像
pip install Flask-SQLAlchemy PyMySQL


# 安装Flask-Migrate数据迁移插件
pip install Flask-Migrate
```



### 3、连接mysql

先创建一个`exts.py`文件，专门管理第三方插件：

```python
# exts.py：插件管理

# 1.导入第三方插件
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# 2.初始化
db = SQLAlchemy()
migrate = Migrate()


# 3.和app对象绑定
def init_exts(app):
    db.init_app(app)
    migrate.init_app(app, db)
```

然后在`__init__.py`文件中设置mysql连接：

```python
# __init__.py: 初始化，创建Flask应用
from flask import Flask

from .exts import init_exts
from .views import main_bp


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

    return app
```



### 4、创建数据模型

创建`models.py`文件：

```python
from .exts import db


# 模型model：类
class User(db.Model):
    # 表名称
    __tablename__ = 't_user'
    # 字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False, default=0)
```



### 5、数据迁移

```bash
# 首先在.views.py文件中导入模型 【如果不导入，模型相关代码不会执行，数据迁移会找不到相关的数据表】
from .models import *
```

在命令行中执行以下命令来初始化迁移目录：

```bash
# 这将在你的项目根目录下创建一个 migrations 文件夹，只需要执行一次
flask db init

# 生成迁移脚本，会自动检测到继承了db.Model的类，自动转为sql语句
flask db migrate

# 应用最新的迁移脚本到数据库【需要提前将数据库创建好】
flask db upgrade

# 如果要撤销操作
flask db downgrade
```

最后打开navicat就能看到已经创建好的表了。

> 注意：如果修改了models文件中表结构，则需要重新生成迁移脚本并应用！



### 6、增删改查

增删改：

```python
from flask import Blueprint, request, render_template, jsonify, make_response, Response, redirect, url_for, session
# 导入模型【如果不导入，模型相关代码不会执行，数据迁移会找不到相关的数据表】
from .models import *

main_bp = Blueprint('main', __name__)

# 添加用户
@main_bp.route('/addUser', methods=['POST'])
def add_user():
    username = request.form.get('username')
    age = request.form.get('age')
    email = request.form.get('email')
    user = User(username=username, age=age, email=email)
    db.session.add(user)
    db.session.commit()
    return '添加成功'


# 添加多个用户
@main_bp.route('/addAllUser')
def add_all_user():
    # 循环10次
    users = []
    for i in range(10):
        user = User(username=f'user{i + 10}', age=i, email=f'user{i + 10}@qq.com')
        users.append(user)

    try:
        db.session.add_all(users)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        db.session.flush()
        return '添加失败: ' + str(e)

    return '添加成功'


# 删除用户
@main_bp.route('/delUser/<int:uid>', methods=['DELETE'])
def del_user(uid):
    user = User.query.get(uid)
    db.session.delete(user)
    db.session.commit()
    return '删除成功'


# 修改用户email
@main_bp.route('/updateUser/<int:uid>', methods=['PUT'])
def update_user(uid):
    user = User.query.get(uid)
    user.email = 'new_email@qq.com'
    db.session.commit()
    return '修改成功'
```

查询：

```python
# 查询单个用户
@main_bp.route('/getUser/<int:uid>', methods=['GET'])
def get_user(uid):
    user = User.query.get(uid)
    # 打印用户和属性
    print(user.id, user.username, user.age, user.email)
    # 返回json数据
    return jsonify(user.as_dict())


# 查询所有用户
@main_bp.route('/getAllUser', methods=['GET'])
def get_all_user():
    users = User.query.all()
    # 打印所有用户和属性
    for user in users:
        print(user.id, user.username, user.age, user.email)
    # 返回json数据
    return jsonify([user.as_dict() for user in users])


# 条件查询用户
@main_bp.route('/getUserByCondition', methods=['GET'])
def get_user_by_condition():
    users = User.query.filter(User.age > 5).all()
    return jsonify([user.as_dict() for user in users])


# 分页查询用户，查询第二页，每页两条
@main_bp.route('/getUserByPage', methods=['GET'])
def get_user_by_page():
    print(222)
    users = User.query.paginate(page=2, per_page=3, error_out=False).items
    # 判断users是否有数据
    if users:
        return jsonify([user.as_dict() for user in users])
    else:
        return '没有数据'


# 分页查询用户，查询第二页，每页两条，要求查询用户的年龄都是大于10的，并且倒序排列
@main_bp.route('/getUserByPageAndCondition', methods=['GET'])
def get_user_by_page_and_condition():
    users = User.query.filter(User.age > 10).order_by(User.age.desc()).paginate(page=2, per_page=3,
                                                                                error_out=False).items
    # 判断users是否有数据
    if users:
        return jsonify([user.as_dict() for user in users])
    else:
        return '没有数据'


# 分页查询用户，查询第二页，每页两条，要求查询用户的年龄大于2，同时返回满足条件的总页数和总条数
@main_bp.route('/getUserByPageAndConditionAndCount', methods=['GET'])
def get_user_by_page_and_condition_and_count():
    users = User.query.filter(User.age > 2).paginate(page=2, per_page=3, error_out=False)
    # 判断users是否有数据
    if users:
        return jsonify({
            'users': [user.as_dict() for user in users.items],
            'total': users.total,
            'pages': users.pages
        })
    else:
        return '没有数据'
```



### 7、多表关联查询

一对多：

```python
# 模型model：文章类，字段为id、title、content、author_id，author_id为外键，指向User表的id字段
class Article(db.Model):
    __tablename__ = 't_article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('t_user.id'), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# 条件查询文章列表，查询作者id为3的所有记录，并且每条记录查询出作者姓名
@main_bp.route('/getArticleByAuthorId', methods=['GET'])
def get_article_by_author_id():
    articles = (Article.query.filter(Article.author_id == 3).join(User)
                .with_entities(Article.id, Article.title, Article.content, User.username).all())
    print(articles)
    return jsonify([(article.id, article.title, article.content, article.username) for article in articles])
```

多对多：

```python
# 模型model：课程类，字段为id、name
class Course(db.Model):
    __tablename__ = 't_course'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# 模型model：选课类，字段为id、student_id、course_id，student_id和course_id为外键，指向User和Course表的id字段
class CourseSelection(db.Model):
    __tablename__ = 't_course_selection'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('t_user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('t_course.id'), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__}
    
    
# 条件查询所有用户的选课情况，返回结果包括用户姓名、课程名称
@main_bp.route('/getCourseSelectionByUser', methods=['GET'])
def get_course_selection_by_user():
    course_selections = (CourseSelection.query.join(User).join(Course)
                         .with_entities(User.username, Course.name).all())
    print(course_selections)
    return jsonify([(course_selection.username, course_selection.name) for course_selection in course_selections])
```



## flask进阶



### 1、flask插件

flas-caching：

```python
# 安装
pip install flask-caching

# 初始化
from flask_caching import Cache

cache = Cache(config={
    # 使用简单的内存缓存
    'CACHE_TYPE': 'simple',
    # 设置缓存的默认过期时间为60秒
    'CACHE_DEFAULT_TIMEOUT': 60
})

# 绑定app
def init_exts(app):
    cache.init_app(app)

# 使用缓存
@main_bp.route('/cacheTest', methods=['GET'])
@cache.cached(timeout=60)
def index_by_cache():
    print('index1')

    # 这里睡眠5秒，首次访问接口在5s后响应，但是后续访问接口在5s内响应
    time.sleep(5)
    return 'index2'
```



### 2、钩子函数

> 什么是钩子函数？
>
> 钩子或者钩子函数，是指在执行函数和目标函数之间挂载的函数，框架开发者给调用方提供一个point挂载点，是一种AOP切面编程思想。
>
>  
>
> 常用的钩子函数：
>
> 1. before_first_request：处理第一次请求之前执行
> 2. before_request：在每次请求之前执行，通常使用这个钩子函数预处理一些变量，实现反爬等
> 3. after_request：注册一个函数，如果没有未处理的异常抛出，在每次请求之后执行
> 4. teardown_appcontext：当APP上下文被移除之后执行的函数，可以进行数据库的提交或者回滚



举个例子：使用AOP反爬策略

```python
# 利用缓存反爬，相同的ip地址1秒内不允许重复访问
@main_bp.before_request
def before_request():
    print('before_request')
    # 打印当前请求的ip地址
    print('ip地址：' + request.remote_addr)
    # 打印当前请求的完整路径
    print('请求url：' + request.url)
    # 打印当前请求的路径，不包含ip地址和路径参数
    print('请求路径：' + request.path)

    # 使用cache缓存当前请求的ip地址和请求时间，和请求路径
    ip = request.remote_addr
    if cache.get(ip):
        return '访问过于频繁，请稍后再试'
    else:
        cache.set(ip, request.remote_addr, timeout=1)
```



### 3、四大内置对象

```
g:
	global全局对象
	g对象是专门用来保存用户的数据的
	g对象在一次请求中的所有的代码的地方，都是可以使用的
	突破变量存储位置的限制，为数据传递添加了新的方式，比如我们在before_request产生一个数据在后面需要使用，可以保存在g对象中，在其它视图函数中就可以使用这个数据
	
reuquest:
	请求对象，可以获取客户端提交过来的所有请求信息
	
session:
	会话技术，服务端会话技术的接口
	
current_app:
	app的配置信息，app对象获取，current_app
	使用获取当前app需要注意，一定要在程序初始化完成之后
```

使用：

```python
from flask import Blueprint, request, render_template, jsonify, make_response, Response, redirect, url_for, session, g, current_app

# 在进入请求之前定义g对象
@main_bp.before_request
def before_request():
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


# 全局内置对象
@main_bp.route('/', methods=['GET'])
@cache.cached(timeout=20)
def index():
    print(g.star)
    return 'hello world111'


# 全局内置对象
@main_bp.route('/test', methods=['GET'])
@cache.cached(timeout=20)
def test():
    print(g.star)
    return 'test'


# current_app内置对象
@main_bp.route('/test2', methods=['GET'])
def test2():
    print(current_app)
    print(current_app.config)
    return 'test2'
```



## 前后端分离restful

当我们使用前后端分离，使用flask-restful插件后就不需要使用蓝图Blueprint插件了。



### 1、基本使用

安装：

```python
# 安装
pip install flask-restful

# 初始化并绑定app
from flask_restful import Api

api = Api()
def init_exts(app):
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    api.init_app(app)
```

定义类视图`apis.py`：

```python
from flask_restful import Resource


# 创建类视图
class UserResource(Resource):
    def get(self):
        return 'get请求'

    def post(self):
        return 'post 请求'
```

定义url路由文件`urls.py`：

```python
from .exts import api
from .apis import *

# 路由
api.add_resource(UserResource, '/user')
```

在`__init__.py`中初始化url路由文件：

```python
from .urls import *
```

访问测试：

```bash
http://127.0.0.1:5000/user

# 输出
"get请求"
```



### 2、字段格式化

使用fields进行定义，通过结合marshal_with来使用。

```python
# 测试字段格式化
ret_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'age': fields.Integer,
    # 'email': fields.String
    'hobby': fields.String(default='暂无')
}


class TestFieldFormatResource(Resource):
    @marshal_with(ret_fields)
    def get(self):
        return {
            'id': 1,
            'username': 'user1',
            'age': 18,
            'email': 'user1@qq.com'
        }
```



### 3、参数解析

解析前端发送过来的数据。

```python
# 测试参数解析
parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='用户名不能为空')
parser.add_argument('age', type=int, required=True, help='年龄不能为空')


class TestParamParserResource(Resource):
    def get(self):
        # 获取参数
        args = parser.parse_args()
        username = args['username']
        age = args['age']
        print(username, age)
        return 'username: ' + username + ' age: ' + str(age)
```









































