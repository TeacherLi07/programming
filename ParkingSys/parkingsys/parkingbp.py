# -*- coding: utf-8 -*- 
# @Time : 2019/12/1 7:42 下午 
# @Author : Lian 
# @Site :
# @File : parkingbp.py
from datetime import datetime
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort
from parkingsys.parkingFee import cal_parking_fee
from parkingsys.db import (
    db_search, db_insert, db_get_all, db_get_car, db_update, db_delete,
    db_get_inlot_car_by_plate
)

bp = Blueprint('parking', __name__)

from . import errors


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def cmp_datetime(a, b):
    a_datetime = datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
    b_datetime = datetime.strptime(b, '%Y-%m-%d %H:%M:%S')

    if a_datetime > b_datetime:
        return -1
    elif a_datetime < b_datetime:
        return 1
    else:
        return 0


def verify_datetime_str(datetime_str):

    try:
        datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def cal_cars_parkingfee(cars):
    for car in cars:
        car["parking_fee"] = ""
        if not ((car["checkout_time"] is None) or str(car["checkout_time"]) == ""):
            car["parking_fee"] = cal_parking_fee(car["checkin_time"], car["checkout_time"])


@bp.route('/')
def index():
    cars = db_get_all()
    cal_cars_parkingfee(cars)
    return render_template('cars.html', cars=cars)


@bp.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == "POST":
        car_plate = request.form['car_plate']
        if not car_plate:
            flash('请输入车牌号码或车牌号码的部分字符！')
        cars = db_search(car_plate)
        cal_cars_parkingfee(cars)
        return render_template('cars.html', cars=cars)
    return render_template('cars.html')


@bp.route('/create', methods=('GET', 'POST'))
def create():
    try:
        if request.method == 'POST':
            car_plate = request.form['car_plate']
            checkin_time = request.form['checkin_time']
            # checkout_time = request.form['checkout_time']

            if not car_plate:
                raise InputError('car_plate', '请输入车牌信息！')

            if not checkin_time:
                raise InputError('checkin_time', '请输入入场时间！')
            else:
                if not verify_datetime_str(checkin_time):
                    raise InputError('checkin_time', '时间格式错误！')

            car = db_get_inlot_car_by_plate(car_plate)
            if car and not car['checkout_time']:
                raise InputError('car_info', '车辆已在库中！')

            db_insert(car_plate, checkin_time)
            return redirect(url_for('parking.index'))

    except InputError as e:
        flash(e.message)

    return render_template('create.html')


def get_car(id):
    car = db_get_car(id)
    if car is None:
        abort(404, "对应编号{0}的车辆未找到。".format(id))

    return car


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
def update(id):
    car = get_car(id)

    try:
        if request.method == 'POST':
            car_plate = request.form['car_plate']
            checkin_time = request.form['checkin_time']
            checkout_time = request.form['checkout_time']

            if not car_plate:
                raise InputError('car_plate', '请输入车牌信息！')

            if not checkin_time:
                raise InputError('checkin_time', '请输入入场时间！')
            else:
                if not verify_datetime_str(checkin_time):
                    raise InputError('checkin_time', '入场时间格式错误！')

            if checkout_time and not verify_datetime_str(checkout_time):
                raise InputError('checkout_time', '出场时间格式错误！')

            # if not checkout_time:
            #    raise InputError('checkout_time', '请输入出场时间！')

            if checkout_time and cmp_datetime(checkin_time, checkout_time) < 0:
                raise InputError('time difference error', '出场时间需晚于入场时间！')

            db_update(id, car_plate, checkin_time, checkout_time)
            return redirect(url_for('parking.index'))

    except InputError as e:
        flash(e.message)

    return render_template('update.html', car=car)


@bp.route('/<int:id>/delete', methods=('POST', 'GET'))
def delete(id):
    db_delete(id)
    return redirect(url_for('parking.index'))


@bp.route('/parkingfee')
def parkingfee():
    a = request.args.get('starttime', '')
    b = request.args.get('endtime', '')
    return jsonify(result=cal_parking_fee(a, b))


@bp.route('/query', methods=('GET', 'POST'))
def query():
    if request.method == "POST":
        # 从网页中获取车牌
        car_plate = request.form['car_plate'].strip()
        # 如果没有填写，则提示用户输入正确的车牌
        if not car_plate:
            flash('请输入车牌号码！')
            return render_template('query.html', car_plate='', checkin_time='', checkout_time='', fee='')
        # 查询所有符合条件的车辆，保存在cars中
        cars = db_search(car_plate)
        try:
            # 取第一条符合条件的记录，放到car中（第一条的序号为0）
            # 如果这里取第一条记录失败，即没有符合条件的记录，会转到except部分执行
            car = cars[0]
            # 为这辆车计算停车费用；如果没有出场时间，则以当前时间计算预估车费
            fee = cal_parking_fee(car['checkin_time'], car['checkout_time'])
            # 渲染生成用户界面，提供车牌、入场时间、出场时间和停车费4项信息，可以用于网页的显示需要
            return render_template('query.html', car_plate=car['car_plate'],
                                   checkin_time=car['checkin_time'], checkout_time=car['checkout_time'], fee=fee)
        except:
            # 如果没有符合条件的车辆，则触发异常，提示没有找到车辆
            flash('未找到车牌为' + car_plate +'的车辆')
            return render_template('query.html', car_plate='', checkin_time='', checkout_time='', fee='')
    else:
        return render_template('query.html', car_plate='', checkin_time='', checkout_time='', fee='')
