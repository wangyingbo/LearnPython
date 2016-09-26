#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#使用type（）
print(type(123))

#从oop.py文件中导入test方法
from oop import test
#从oop.py文件中导入run_twice方法
from oop import run_twice
test()


#从oop.py文件中导入Animal类
from oop import Animal
lion = Animal()
print(isinstance(lion, Animal))
run_twice(lion)

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))


# 获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print('获取一个对象的所有属性和方法',dir('ABC'))
print('获得一个字符串的长度',len('ABC'))
print('获得一个字符创的长度','ABC'.__len__())
print('获得一个字符创的小写','ABC'.lower())


# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
class MyDog(object):
	"""docstring for MyDog"""
	def __len__(self):
		return 100

	def __test__(self):
		return print('test a custom method')

dog = MyDog()
print('自定义len' ,len(dog))
dog.__test__()


class MyObject(object):
	"""docstring for MyObject"""
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

obj = MyObject()
print('有属性x没有？',hasattr(obj,'x')) #有没有属性‘x’
print(obj.x)
print('有属性y没有？',hasattr(obj,'y')) #有没有属性‘y’
setattr(obj, 'y', 19) # 设置一个属性'y'
print('调用setattr后，有属性y没有？',hasattr(obj,'y')) # 有属性'y'吗？
print('获得属性y',getattr(obj, 'y')) # 获取属性'y'
print(obj.y) # 获取属性'y'
print('获取不存在的属性，抛出默认值', getattr(obj,'z',404))

		







