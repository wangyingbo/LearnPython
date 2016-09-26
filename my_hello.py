#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Hello import Hello
h = Hello()
h.my_hello()
print(type(Hello))
print(type(h))


def fn(self,name='wangyingbo'):
	print('Hellooom, %s.' % name)
Wang_hello = type('Wang_hello',(object,),dict(wang_hello=fn))
h1=Wang_hello()
h1.wang_hello()