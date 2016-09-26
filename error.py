#!/usr/bin/env python3
# -*- coding: utf-8 -*-


try:
	print('try......')
	r = 10/int('a')
	print('result:',r)
except ValueError as e:
	print('ValueError:',e)
except ZeroDivisionError as e:
	print('except:',e)
else:
	print('else......')
finally:
	print('finally......')
print('end')


# 比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')







