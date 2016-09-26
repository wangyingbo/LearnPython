#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 打开一个jpg图片文件，注意是当前路径
im = Image.open('test.jpg')
# 获得图片尺寸
w,h = im.size
print('Original image size is : %sx%s' % (w,h))
# 缩放到50%
# im.thumbnail((w/2,h/2))
# print('Resize image to : %sx%s' % (w/2,h/2))
# im.save('thumbnail.jpg','jpeg')


# 当前路径打开一张图片，做模糊效果
im = Image.open('test.jpg')
# 应用模糊滤镜
# im1 = im.filter(ImageFilter.BLUR)
# im1.save('blur.jpg','jpeg')


# 随机字母：
def rndChar():
	return chr(random.randint(65,90))
# 随机颜色1：
def rndColor():
	return (random.randint(64,255), random.randint(64,255), random.randint(64,255))
# 随机颜色2：
def rndColor2():
	return (random.randint(64,127), random.randint(64,127), random.randint(64,127))
width = 60 * 4
height = 60
image = Image.new('RGB',(width,height),(255,255,255))
# 创建Font对象：
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象：
draw = ImageDraw.Draw(image)
# 填充每个像素：
for x in xrange(width):
	for y in range(height):
		draw.point((x,y), fill = rndColor())
# 输出文字：
for t in xrange(4):
	draw.text((60 * t + 10,10),rndChar(),font = font, fill = rndColor2())
# 模糊：
image = Image.filter(ImageFilter.BLUR)
image.save('code_creat.jpg','jpeg')








