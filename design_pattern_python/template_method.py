#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   template_method.py
@Time    :   2021/01/28 12:20:10
@Author  :   Ayden Zeng
@Version :   1.0
@Contact :   aydenzeng@163.com
@License :   (C)Copyright 2020-2021, Ayden-Zeng-Private
@Desc    :   None
'''

# here put the import lib
from abc import abstractmethod, ABCMeta
from time import sleep

class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def repaint(self):
        pass
    
    # 定义算法骨架，即一个模板方法
    def run(self):
        self.start()
        while True:
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()


# 具体类
class MyWindow(Window):
    def __init__(self, msg):
        self.msg = msg
        
    def start(self):
        print("开始运行窗口")
    
    def stop(self):
        print("结束运行窗口")
    
    def repaint(self):
        print(self.msg)


# Client
w = MyWindow("Hello...")
w.run()
