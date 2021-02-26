#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   proxy.py
@Time    :   2021/01/25 09:45:27
@Author  :   Ayden Zeng
@Version :   1.0
@Contact :   aydenzeng@163.com
@License :   (C)Copyright 2020-2021, Ayden-Zeng-Private
@Desc    :   None
'''

# here put the import lib
from abc import abstractmethod, ABCMeta

# 抽象实体
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


#  实体
class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(self.filename, 'r')
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'a')
        f.write(content, )
        f.close()


# 虚代理：只有当调用get_content()方法时才开辟内存读取文件
#         而不是在实例化时就读取文件，造成内存占用
class VirtualSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.sub = None

    def get_content(self):
        if self.sub is None:
            sub = RealSubject(self.filename)
            self.content = sub.content
        return self.content

    def set_content(self, content):
        if self.sub is None:
            sub = RealSubject(self.filename)
        sub.set_content(content)


# client
filename = './test.txt'
subject = VirtualSubject(filename)  # 不会读取该文件占用内存
subject.get_content()  # 此时才会读取文件
content = "zyb tai qiang le\n"
subject.set_content(content)


# 保护代理：在写入文件时，提示无权限进行保护
class ProtectSubject(Subject):
    def __init__(self, filename):
        self.sub = RealSubject(filename)
    
    def get_content(self):
        return self.sub.get_content()
    
    def set_content(self, content):
        raise PermissionError("无写入权限")

# client
subject = ProtectSubject('./test.txt')
subject.set_content("ni shi zhen de nb\n")  # raise error
