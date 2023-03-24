import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from extensions import db
import config
from models import OrderInformation
from blueprints.Unallocated import bp as unallocated_bp
from flask_migrate import Migrate

app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)
# 意思是在没有配置文件的时候先初始化
db.init_app(app)
Migrate = Migrate(app, db)
# 绑定蓝图
app.register_blueprint(unallocated_bp)

# 设置config.py中配置信息连接数据库

# 视图函数全部放在蓝图当中


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 80)))
