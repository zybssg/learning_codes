#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   adapter.py
@Time    :   2021/01/21 10:17:58
@Author  :   Ayden Zeng
@Version :   1.0
@Contact :   aydenzeng@163.com
@License :   (C)Copyright 2020-2021, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
from abc import abstractmethod, ABCMeta

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print("use alipay to pay %d yuan"%money)


class WechatPay(Payment):
    def pay(self, money):
        print("use wechat to pay %d yuan"%money)

class BankPay:
    def cost(self, money):
        print("use YINLIAN to pay %d yuan"%money)


class ApplePay:
    def cost(self, money):
        print("use applepay to pay %d yuan"%money)


# 方法一：使用多继承适配
# 缺点：每多一个新接口（cost）类（ApplePay)，为了和老接口（pay）适配，就需要重写一个类
class NewBankPay(Payment, BankPay):
    def pay(self, money):
        self.cost(money)


# 方法二：使用组合适配
class PaymentAdaptor(Payment):
    def  __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)

p = NewBankPay()
p.pay(200)

p = PaymentAdaptor(ApplePay())
p.pay(200)
