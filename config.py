# 设置数据库配置信息
HOSTNAME = '127.0.0.1'
DATABASE = 'mysqlproject'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'sql2008'
DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
JSON_AS_ASCII = False
SQLALCHEMY_DATABASE_URI = DB_URL

