#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 接收到的参数依次是：
# 1.当前准备创建的类的对象；
# 2.类的名字；
# 3.类继承的父类的集合；
# 4.类的方法集合
class ListMetaclass(type):
	"""metaclass"""
	def __new__(cls,name,bases,attrs):
		attrs['add'] = lambda self,value:self.append(value)
		return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass = ListMetaclass):
	pass


L = MyList()
L.add(1)	
print(L)
