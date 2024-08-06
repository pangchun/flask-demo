import time

from flask import request, jsonify, g, current_app
from flask_restful import Resource, fields, marshal_with, reqparse

from app.exts import db, cache
from app.models import User, Article, CourseSelection, Course


# 添加用户
class AddUserResource(Resource):
    def post(self):
        # 从form中获取请求参数
        param = request.form
        username = param.get('username')
        age = param.get('age')
        email = param.get('email')
        print(username, age, email)

        # 新增用户到数据库
        user = User(username=username, age=age, email=email)
        db.session.add(user)
        db.session.commit()

        return jsonify(user.as_dict())


# 添加多个用户
class AddAllUserResource(Resource):
    def post(self):
        # 循环10次
        users = []
        for i in range(10):
            user = User(username=f'user{i + 10}', age=i, email=f'user{i + 10}@qq.com')
            users.append(user)

        # 提交事务和异常处理
        try:
            db.session.add_all(users)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            return '添加多用户失败: ' + str(e)

        return '成功添加' + str(len(users)) + '位用户'


# 删除用户
class DelUserResource(Resource):
    def delete(self, uid):
        # 删除用户
        user = User.query.get(uid)
        db.session.delete(user)
        db.session.commit()

        return '成功删除一位用户'


# 修改用户
class UpdateUserResource(Resource):
    def put(self, uid):
        # 获取请求参数
        param = request.form
        username = param.get('username')
        age = param.get('age')
        email = param.get('email')

        # 修改用户
        user = User.query.get(uid)
        user.username = username
        user.age = age
        user.email = email
        db.session.commit()

        return '成功修改一位用户'


# 查询单个用户
class GetUserResource(Resource):
    def get(self, uid):
        user = User.query.get(uid)
        return jsonify(user.as_dict())


# 查询所有用户
class GetAllUserResource(Resource):
    def get(self):
        users = User.query.all()
        return jsonify([user.as_dict() for user in users])


# 条件查询用户
class GetUserByConditionResource(Resource):
    def get(self):
        # 查询用户
        users = User.query.filter(User.age > 5).all()
        return jsonify([user.as_dict() for user in users])


# 分页查询用户 【查询第一页，每页两条，要求查询用户的年龄都是大于0的，并且倒序排列】
class GetUserByPageResource(Resource):
    def get(self):
        users = User.query.filter(User.age > 0).order_by(User.age.desc()).paginate(page=1, per_page=2, error_out=False)
        # 判断users是否有数据
        if users:
            return jsonify({
                'users': [user.as_dict() for user in users.items],
                'total': users.total,
                'pages': users.pages
            })
        else:
            return '没有数据'


# 联表查询文章-作者
class GetArticleResource(Resource):
    def get(self):
        articles = (Article.query.filter(Article.author_id == 3).join(User)
                    .with_entities(Article.id, Article.title, Article.content, User.username).all())
        print(articles)
        return jsonify([(article.id, article.title, article.content, article.username) for article in articles])


# 联表查询选课-课程-学生
class GetCourseSelectionResource(Resource):
    def get(self):
        course_selections = (CourseSelection.query.join(User).join(Course)
                             .with_entities(User.username, Course.name).all())
        print(course_selections)
        return jsonify([(course_selection.username, course_selection.name) for course_selection in course_selections])


# 测试缓存
class TestCacheResource(Resource):
    @cache.cached(timeout=60)
    def get(self):
        print('index1')

        # 这里睡眠5秒，首次访问接口在5s后响应，但是后续访问接口在5s内响应
        time.sleep(5)
        return 'index2'


# 测试global内置对象
class TestGlobalObjResource(Resource):
    def get(self):
        print(g.star)
        return 'hello world'


# 测试current_app内置对象
class TestCurrentAppResource(Resource):
    def get(self):
        print(current_app)
        print(current_app.config)
        return 'hello world'


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
