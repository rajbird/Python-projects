#!/usr/bin/python

import Tkinter
import tkMessageBox
import sys
import Tkinter
import tkMessageBox
import math
from Tkinter import *
import tkFileDialog

#
#Checks if the domain and range was entered
#
def checkDomainRange():
	global domain_data, range_data
	if domain_data.get() == "":
		tkMessageBox.showinfo("Error", "Set Domain")
		return False
	if range_data.get() == "":
		tkMessageBox.showinfo("Error", "Set Range")
		return False
#
#Determine if basic or graph should be called,
#calls the appropriate function from calcMath
#
def play():
	import calcMath
	global modeLabel, label, domain_data

	if label.get() == "":
		return

	if modeLabel.get() == "Basic":
		#Basic math
		label.set(calcMath.basicMath(label.get(), 1))
		
	elif modeLabel.get() == "Graph":
		if checkDomainRange() == False:
			return
		callPlot(calcMath.graphicMath(label.get(), int(domain_data.get())))

#
#Draws the quadrant for the graph
#
def drawGraph():
	global canvas
	canvas.delete("all")
	canvas.create_line(249, 0, 249, 499)
	canvas.create_line(0, 249, 499, 249)
#
#Draws the dots ( given by plot() ) onto the canvas
#
def callPlot(coord):
	import graph
	global domain_data
	drawGraph()

	if coord == None:
		tkMessageBox.showinfo("Error", "Invaild Expression")
		return

	arr = []
	i = 0 #index for x
	j = 1 #index for y
	x = 0
	y = 0

	while True:
		if i > len(coord)-1:
			break
		x = coord[i]
		y = coord[j]
		arr = graph.plot((x,y))
		canvas.create_oval(arr[0],arr[2],arr[1],arr[3], outline='blue')
		i = i + 2
		j = j + 2
		if x == (int(domain_data.get())):
			break

#
#Apply domain and range changes
#
def enterDR():
	import graph

	if checkDomainRange() == False:
		return

	graph.domain(int(domain_data.get()), int(range_data.get()))

#
#Changes the string in the view
#parameter: str to be appended
#
def viewChange(num):
	global label
	global modeLabel
	operators = {'+', '-', '/', '*', '.','^'}
	letters = {'l', 's', 'c', 't'}
	s = label.get()
	pre = ""


	if modeLabel.get() == "Graph":
		tag = "y = "
	else:
		tag = ""

	try:
		if num == "x" and s[len(s)-1].isdigit():
			pre = prev(label.get())
			AC()
			label.set(tag+pre+"*"+num)	
			return
	except Exception, e:
		pass

	if num in operators:
		if len(s) == 0:
			return
		if s[len(s)-1] in operators or s[len(s)-1] == '(':
			return 
	try:
		if s[len(s)-1] == ')':
			if num.isdigit() or num[0] in letters or num == 'x':
				pre = prev(label.get())
				AC()
				label.set(tag+pre+"*"+num)	
				return
	except:
		pass
	if num == '(':
		try:
			if s[len(s)-1] not in operators and s[len(s)-1] != ' ':
				pre = prev(label.get())
				AC()
				label.set(tag+pre+"*(")
				return
		except:
			pass
	try:
		if s[len(s)-1] == 'x' and num not in operators and num != ')':
				pre = prev(label.get())
				AC()
				label.set(tag+pre+"*"+num)	
				return
	except Exception, e:
		pass

	pre = prev(label.get())
	AC()
	label.set(tag+pre+num)

#
#Removes the "y = ", if it exists
#
def prev(str):
	if str[:4] == "y = ":
		return str[4:]
	else:
		return str

#
#Deletes one charater from the string 
#
def DEL():
	global label
	pre = label.get()
	pre = pre[:-1]
	label.set(pre)
#
#Clears everything from the view
#
def AC():
	global label
	label.set("")
#
#Saves the view string
#
def MS():
	global label
	global MSvar
	MSvar = prev(label.get())

#
#Returns the saved string
#
def MR():
	global label
	global MSvar
	label.set(label.get()+MSvar)

#
#For mode changes
#
def mode():
	global label
	global modeLabel
	global btnX
	if modeLabel.get() == "Basic":
		modeLabel.set("Graph")
		btnX.config(state = NORMAL)
		label.set("y = ")
	else:
		btnX.config(state = DISABLED)
		modeLabel.set("Basic")
		label.set("")		

#
#Main body
#

root = Tkinter.Tk()
root.title("Calculator")
offset = 3
label = StringVar()
modeLabel = StringVar()
MSvar = ""
modeLabel.set("Basic")

canvas = Tkinter.Canvas(root, bg="white", height="500", width="500")
canvas.grid(rowspan=250)

keypad = Tkinter.Frame(root).grid()

drawGraph()	#drawing the quadrant


#Basic math view
view = Tkinter.Label(root, textvariable=label, bg="white", height=3, width=81).grid(row=-3+offset, column=1, columnspan=6, sticky="W")

#sqrt
DB = Button(root, text ="sqrt", command = lambda: viewChange("sqrt("), height=2, width=10)
DB.grid(row=0+offset, column=6)

#Basic or Graph mode
btnMode = Tkinter.Button(keypad, textvariable=modeLabel, height=2, width=10, command = mode).grid(row=-1+offset, column=6)

#button for the 'x' variable
btnX = Tkinter.Button(keypad, text="x", height=2, width=10, command = lambda: viewChange("x"))
btnX.grid(row=4+offset, column=1)
btnX.config(state = DISABLED) #disabling it because calculator starts off in basic mode

#Special function buttons 
btnSIN = Tkinter.Button(keypad, text="sin", height=2, width=10, command = lambda: viewChange("sin(")).grid(row=-1+offset, column=1)
btnSIN1 = Tkinter.Button(keypad, text="csc", height=2, width=10, command = lambda: viewChange("csc(")).grid(row=0+offset, column=1)
btnCOS = Tkinter.Button(keypad, text="cos", height=2, width=10, command = lambda: viewChange("cos(")).grid(row=-1+offset, column=2)
btnCOS1 = Tkinter.Button(keypad, text="sec", height=2, width=10, command = lambda: viewChange("sec(")).grid(row=0+offset, column=2)
btnTAN = Tkinter.Button(keypad, text="tan", height=2, width=10, command = lambda: viewChange("tan(")).grid(row=-1+offset, column=3)
btnTAN1 = Tkinter.Button(keypad, text="cot", height=2, width=10, command = lambda: viewChange("cot(")).grid(row=0+offset, column=3)
btnPower = Tkinter.Button(keypad, text="^", height=2, width=10, command = lambda: viewChange("^")).grid(row=-1+offset, column=4)
btnlog = Tkinter.Button(keypad, text="log", height=2, width=10, command = lambda: viewChange("log(")).grid(row=-1+offset, column=5)
btnPi = Tkinter.Button(keypad, text="pi", height=2, width=10, command = lambda: viewChange("3.141593")).grid(row=0+offset, column=4)
btnln = Tkinter.Button(keypad, text="ln", height=2, width=10, command = lambda: viewChange("ln(")).grid(row=0+offset, column=5)

#Memory buttons
btnMS = Tkinter.Button(keypad, text="MS", height=2, width=10, command = MS).grid(row=1+offset, column=5)
btnMR = Tkinter.Button(keypad, text="MR", height=2, width=10, command = MR).grid(row=1+offset, column=6)

#Parentheses
btnOpenP = Tkinter.Button(keypad, text="(", height=2, width=10, command = lambda: viewChange("(")).grid(row=2+offset, column=5)
btnCloseP = Tkinter.Button(keypad, text=")", height=2, width=10, command = lambda: viewChange(")")).grid(row=2+offset, column=6)

#Deleting and clearing
btnDEL = Tkinter.Button(keypad, text="DEL", height=2, width=10, command = DEL).grid(row=3+offset, column=5)
btnAC = Tkinter.Button(keypad, text="AC", height=2, width=10, command = AC).grid(row=3+offset, column=6)

#Equals button (calls play)
btnEqual = Tkinter.Button(keypad, text="=", height=2, width=24, command = play).grid(row=4+offset, column=5, columnspan=2, sticky="W")

#Operations buttons
btnPlus = Tkinter.Button(keypad, text="+", height=2, width=10, command = lambda: viewChange("+")).grid(row=1+offset, column=4)
btnMinus = Tkinter.Button(keypad, text="-", height=2, width=10, command = lambda: viewChange("-")).grid(row=2+offset, column=4)
btnMul = Tkinter.Button(keypad, text="*", height=2, width=10, command = lambda: viewChange("*")).grid(row=3+offset, column=4)
btnDiv = Tkinter.Button(keypad, text="/", height=2, width=10, command = lambda: viewChange("/")).grid(row=4+offset, column=4)

#7, 8, 9
btn7 = Tkinter.Button(keypad, text="7", height=2, width=10, command = lambda: viewChange("7")).grid(row=1+offset, column=1)
btn8 = Tkinter.Button(keypad, text="8", height=2, width=10, command = lambda: viewChange("8")).grid(row=1+offset, column=2)
btn9 = Tkinter.Button(keypad, text="9", height=2, width=10, command = lambda: viewChange("9")).grid(row=1+offset, column=3)

#4, 5, 6
btn4 = Tkinter.Button(keypad, text="4", height=2, width=10, command = lambda: viewChange("4")).grid(row=2+offset, column=1)
btn5 = Tkinter.Button(keypad, text="5", height=2, width=10, command = lambda: viewChange("5")).grid(row=2+offset, column=2)
btn6 = Tkinter.Button(keypad, text="6", height=2, width=10, command = lambda: viewChange("6")).grid(row=2+offset, column=3)

#1, 2, 3
btn1 = Tkinter.Button(keypad, text="1", height=2, width=10, command = lambda: viewChange("1")).grid(row=3+offset, column=1)
btn2 = Tkinter.Button(keypad, text="2", height=2, width=10, command = lambda: viewChange("2")).grid(row=3+offset, column=2)
btn3 = Tkinter.Button(keypad, text="3", height=2, width=10, command = lambda: viewChange("3")).grid(row=3+offset, column=3)

#0 and period
btn0 = Tkinter.Button(keypad, text="0", height=2, width=10, command = lambda: viewChange("0")).grid(row=4+offset, column=2)
btnDot = Tkinter.Button(keypad, text=".", height=2, width=10, command = lambda: viewChange(".")).grid(row=4+offset, column=3)

#Domain
domain_text = Tkinter.Label(keypad, text="Domain").grid(row=5+offset, column=6)
domain_data = Tkinter.Entry(keypad,width=10)
domain_data.grid(row=6+offset, column=6)

#Range
range_text = Tkinter.Label(keypad, text="Range").grid(row=7+offset, column=6)
range_data = Tkinter.Entry(keypad,width=10)
range_data.grid(row=8+offset, column=6)

btnUser = Tkinter.Button(keypad, text="Enter", height=2, width=10, command = enterDR).grid(row=9+offset, column=6)


root.mainloop()
