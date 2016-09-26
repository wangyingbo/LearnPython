#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	"""Dog从Animal类继承而来"""
	def run(self):
		print('Dog is running...')

class Cat(Animal):
	"""Cat从Animal类继承而来"""
	def run(self):
		print('Cat is running...')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

a = list()

print('dog is Dog?', isinstance(dog, Dog))
print('cat is Cat?', isinstance(cat, Cat))
print('a is list?',isinstance(a, list))


def run_twice(myArg):
	myArg.run()
	myArg.run()

def test():
	print('test')

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):
	"""docstring for Tortoise"""
	def run(self):
		print('Tortoise is running slowly...')

run_twice(Tortoise())


#对于静态语言（例如Java）来说，如果需要传入Animal类型，
#	则传入的对象必须是Animal类型或者它的子类
#	否则，将无法调用run()方法。

#对于Python这样的动态语言来说，则不一定需要传入Animal类型。
#	我们只需要保证传入的对象有一个run()方法就可以了：

#	class Timer(object):
#	    def run(self):
#	        print('Start...')

#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
#	一个对象只要“看起来像鸭子，走起路来像鸭子”，
#	那它就可以被看做是鸭子。


		


		