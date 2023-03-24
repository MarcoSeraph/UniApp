from extensions import db


class OrderInformation(db.Model):
    __tableName__ = "OrderInformation"   # 设置表名
    ClientId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ClientName = db.Column(db.String(30), nullable=True)
    PhoneNumber = db.Column(db.String(20), unique=True)
    Address = db.Column(db.String(100), nullable=True)
    Region = db.Column(db.String(20), nullable=True)  # 省份
    City = db.Column(db.String(20), nullable=True)  # 市
    District = db.Column(db.String(20), nullable=True)
    Demand = db.Column(db.Text, nullable=True)
    Delivery = db.Column(db.Date, nullable=True)
    IsUrgentFlag = db.Column(db.Enum('1', '0'))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class CarProducts(db.Model):
    __tableName__ = "CarProducts"
    CarId = db.Column(db.Integer,primary_key=True, autoincrement=True)
    CarName = db.Column(db.String(20))
    Supplier = db.Column(db.String(20))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
