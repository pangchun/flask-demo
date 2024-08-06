from .exts import api
from .apis import *

# 用户路由
api.add_resource(AddUserResource, '/addUser')
api.add_resource(AddAllUserResource, '/addAllUser')
api.add_resource(DelUserResource, '/delUser/<int:uid>')
api.add_resource(UpdateUserResource, '/updateUser/<int:uid>')
api.add_resource(GetUserResource, '/getUsergetUser/<int:uid>')
api.add_resource(GetAllUserResource, '/getAllUser')
api.add_resource(GetUserByConditionResource, '/getUserByCondition')
api.add_resource(GetUserByPageResource, '/getUserByPage')

# 文章路由
api.add_resource(GetArticleResource, '/getArticle')

# 选课路由
api.add_resource(GetCourseSelectionResource, '/getCourseSelection')

# 测试缓存路由
api.add_resource(TestCacheResource, '/testCache')

# 测试global内置对象路由
api.add_resource(TestGlobalObjResource, '/testGlobalObj')

# 测试current_app内置对象路由
api.add_resource(TestCurrentAppResource, '/testCurrentApp')

# 测试字段格式化路由
api.add_resource(TestFieldFormatResource, '/testFieldFormat')

# 测试参数解析
api.add_resource(TestParamParserResource, '/testParser')
