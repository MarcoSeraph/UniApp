import time
from datetime import datetime

from flask import Blueprint, render_template, jsonify, Response,request

import json

from flask_cors import cross_origin

from models import OrderInformation,CarProducts
from extensions import db
# 未分配界面 作为首页
bp = Blueprint("unallocated", __name__, url_prefix="/")

# flask db migrate 将orm迁移脚本
# flask db upgrade 将迁移脚本映射到数据库


def get_time(timestamp):
    time_local = time.localtime(timestamp)
    ret = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return ret


@bp.route('/')
def welcome():
    return "clb"


@bp.route('/order/add', methods=["GET", "POST"])
def add_order():

    # 1.创建 ORM对象
    order = OrderInformation(ClientName="韩昱川", PhoneNumber="19157713936", Address="山东省滨州市博兴县阳光小区2单元4号楼", Region="山东省",
                             City="滨州市", District="博兴县", Demand="50型特厚,液化气,带上大天然气的小钻头", Delivery="2023-03-13", IsUrgentFlag="0")
    # 2. 将ORM对象添加到db.session 中
    db.session.add(order)
    # 3. 将 db.session 中的改变同步到数据库中
    db.session.commit()
    return "订单添加成功"


@bp.route('/order/query',methods=["GET", "POST"])
def query_order():
    # 1. get 查找：根据主键查找  定义orderinformation的时候 继承了db.model 直接使用
    # order = OrderInformation.query.get(1)
    # print(f"{order.ClientId}:{order.ClientName}")
    # return "数据查询成功"
    # 2.通过 filter_by 查找
    orders = OrderInformation.query.filter_by(ClientName="韩昱川")
    for order in orders:
        print(order.ClientName)
    return "数据查询成功"


@bp.route('/order/update',methods=["GET", "POST"])
def update_order():
    order = OrderInformation.query.filter_by(ClientName="韩昱川").first()
    order.PhoneNumber = "15550613275"
    db.session.commit()
    return "数据修改成功"


@bp.route('/order/delete',methods=["GET", "POST"])
def delete_order():
    # 1 查找 获取主键为1 的 数据
    order = OrderInformation.query.get(1)
    # 2 删除
    db.session.delete(order)
    # 3. 将db.session 同步到数据库
    db.session.commit()
    return "数据删除成功"


@bp.route('order/pre')
def convey():
        res = {'msg': '这是一个接口', 'msg_dode': 0}
        return json.dumps(res, ensure_ascii=False)


@bp.route('/products/query',methods=["GET", "POST"])
@cross_origin()
def query_products():
    quest = request.json['what']
    print(quest)
    products = CarProducts.query.all()
    json_list = [];
    json_content = {};
    for product in products:
        json_content = {'CarId': product.CarId,'CarName': product.CarName,'Supplier': product.Supplier}
        json_list.append(json_content)
        json_content = {}
    print("有人发送请求了")
    print(json.dumps(json_list))
    return 'clb'
    # return Response(json.dumps(json_list), mimetype='application/json')
    # return jsonify(json_list)
