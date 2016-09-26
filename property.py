#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# from slots import MyStudent
# mm = MyStudent()
# mm.name = 'Michael'
# print(mm.name)


class Student(object):
	"""docstring for Student"""
	@property
	def score(self):
	    return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100')
		self._score = value

	@property
	def birth(self):
	    return self._birth

	@birth.setter
	def birth(self,value):
		self._birth = value
	
	@property
	def age(self):
	    return 2016-self._birth
	

s = Student()
s.score = 60
print('分数是',s.score)
s.score = 99
print('分数是',s.score)
s.birth = 1991
print('生日是',s.birth)
print('年龄是',s.age)





	
