from .exts import db


# 用户表
class User(db.Model):
    # 表名称
    __tablename__ = 't_user'
    # 字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False, default=0)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# 文章表
class Article(db.Model):
    __tablename__ = 't_article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('t_user.id'), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# 课程表
class Course(db.Model):
    __tablename__ = 't_course'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# 选课表
class CourseSelection(db.Model):
    __tablename__ = 't_course_selection'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('t_user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('t_course.id'), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__}
