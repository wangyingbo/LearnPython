#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	"""docstring for Student"""
	pass
	

def set_age(self, age):  # 定义一个函数作为实例方法
	self.age = age


s = Student()
s.name = 'wangyingbo'
print(s.name)
from types import MethodType
s.set_age = MethodType(set_age, s)  #给实例绑定一个方法
s.set_age(25)  #调用实例方法
print(s.age)


# 但是，给一个实例绑定的方法，对另一个实例是不起作用的
# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
	self.score = score

Student.set_score = set_score
s.set_score(10)
s2 = Student()
s2.set_score(100)
print(s.score)
print(s2.score)


# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class MyStudent(object):
	"""docstring for MyStudent"""
	__slots__ = ('name','age') # 用tuple定义允许绑定的属性名称
	
m = MyStudent()
m.name = 'wang'
m.age = 34
# m.score = 399999  # 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误


# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(MyStudent):
	"""docstring for GraduateStudent"""
	pass

g = GraduateStudent()
g.score = 999999

# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__


		

		



