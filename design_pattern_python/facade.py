#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   facade.py
@Time    :   2021/01/25 09:14:19
@Author  :   Ayden Zeng
@Version :   1.0
@Contact :   aydenzeng@163.com
@License :   (C)Copyright 2020-2021, Ayden-Zeng-Private
@Desc    :   None
'''

# here put the import lib
from  abc import abstractmethod, ABCMeta

class CPU:
    def run(self):
        print("CPU开始运行")
    
    def stop(self):
        print("CPU停止工作")


class Disk:
    def run(self):
        print("硬盘开始运行")
    
    def stop(self):
        print("硬盘停止工作")


class Memory:
    def run(self):
        print("内存开始运行")
    
    def stop(self):
        print("内存停止工作")


# facade
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


# client
computer = Computer()
computer.run()
print("="*10)
computer.stop()
