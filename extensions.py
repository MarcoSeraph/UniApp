# 这个文件存在的意义是处理循环导入问题
# 先创建空的db
# 插件的对象

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
