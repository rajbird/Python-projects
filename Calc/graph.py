from Tkinter import *

canvasX = 500
canvasY = 500

domainX = 500
domainY = 500

scaleX = domainX/float(canvasX)
scaleY = domainY/float(canvasY)

def domain(x,y):
	global domainX, domainY, scaleX, scaleY

	domainX = x
	domainY = y

	scaleX = domainX/float(canvasX)
	scaleY = domainY/float(canvasY)

def plot(coords):
	global x_center, y_center, scaleX, scaleY

	r = 0.01

	x, y = coords


	pointx1 = x_center - r + x/scaleX
	pointx2 = x_center + r + x/scaleX

	pointy1 = y_center - r - y/scaleY
	pointy2 = y_center + r - y/scaleY

	return (pointx1,pointx2, pointy1, pointy2)

x_center = 249
y_center = 248
