#!/usr/bin/python
from Tkinter import *
import tkMessageBox

root = Tk()
C = Canvas(root, bg ="#ffa3fb",height = 630, width = 630)
#C.create_line(215, 0, 215, 644, fill="#ffa3fb", width = 10)
#C.create_line(430, 0, 430, 644, fill="#ffa3fb", width = 10)
#C.create_line(0, 215, 644, 215, fill="#ffa3fb", width = 10)
#C.create_line(0, 430, 644, 430, fill="#ffa3fb", width = 10)

x = PhotoImage(file="x.gif")
o = PhotoImage(file="o.gif")
blank = PhotoImage(file="blank.gif")

location = ["","","","","","","","",""]
player = -1

won = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
def zero():
	global player
	global location
	if player == 1:
		location[0] = "X"
		zero.config(image=x, state = DISABLED)
		player = 2
	else:
		location[0] = "O"
		zero.config(image=o, state = DISABLED)
		player = 1
	winner()

def one():
	global player
	global location
	if player == 1:
		location[1] = "X"
		one.config(image=x, state = DISABLED)
		player = 2
	else:
		location[1] = "O"
		one.config(image=o, state = DISABLED)
		player = 1
	winner()

def two():
	global player
	global location
	if player == 1:
		location[2] = "X"
		two.config(image=x, state = DISABLED)
		player = 2
	else:
		location[2] = "O"
		two.config(image=o, state = DISABLED)
		player = 1
	winner()

def three():
	global player
	global location
	if player == 1:
		location[3] = "X"
		three.config(image=x, state = DISABLED)
		player = 2
	else:
		location[3] = "O"
		three.config(image=o, state = DISABLED)
		player = 1
	winner()

def four():
	global player
	global location
	if player == 1:
		location[4] = "X"
		four.config(image=x, state = DISABLED)
		player = 2
	else:
		location[4] = "O"
		four.config(image=o, state = DISABLED)
		player = 1
	winner()

def five():
	global player
	global location
	if player == 1:
		location[5] = "X"
		five.config(image=x, state = DISABLED)
		player = 2
	else:
		location[5] = "O"
		five.config(image=o, state = DISABLED)
		player = 1
	winner()

def six():
	global player
	global location
	if player == 1:
		location[6] = "X"
		six.config(image=x, state = DISABLED)
		player = 2
	else:
		location[6] = "O"
		six.config(image=o, state = DISABLED)
		player = 1
	winner()

def seven():
	global player
	global location
	if player == 1:
		location[7] = "X"
		seven.config(image=x, state = DISABLED)
		player = 2
	else:
		location[7] = "O"
		seven.config(image=o, state = DISABLED)
		player = 1
	winner()

def eight():
	global player
	global location
	if player == 1:
		location[8] = "X"
		eight.config(image=x, state = DISABLED)
		player = 2
	else:
		location[8] = "O"
		eight.config(image=o, state = DISABLED)
		player = 1
	winner()

def winner():
	xs = 0
	os = 0
	for streak in won:
		for num in streak:
			if(location[num] == "X"):
				xs = xs+1
			elif (location[num] == "O"):
				os = os+1
			else:
				break
		if(xs == 3):
			tkMessageBox.showinfo("Winner", "PLAYER 1 is the winner")
			root.destroy()
			return
		elif(os == 3):
			tkMessageBox.showinfo("Winner", "PLAYER 2 is the winner")
			root.destroy()
			return
		xs = 0
		os = 0

	for slot in location:
		if (slot == ""):
			return
	tkMessageBox.showinfo("Winner", "TIE")
	root.destroy()

zero = Button(root, bg ="#f9ccf8", image = blank , height = 200, width = 200, relief = FLAT, command = zero)
zero.place(x=0, y=0)

one = Button(root, bg ="#f9ccf8", image = blank, command = one, height = 200, width = 200, relief = FLAT)
one.place(x=214,y=0)

two = Button(root, bg ="#f9ccf8", image = blank, command = two, height = 200, width = 200, relief = FLAT)
two.place(x=429,y=0)

three = Button(root, bg ="#f9ccf8", image = blank, command = three, height = 200, width = 200, relief = FLAT)
three.place(x=0,y=214)

four = Button(root, bg ="#f9ccf8", image = blank, command = four, height = 200, width = 200, relief = FLAT)
four.place(x=214,y=214)

five = Button(root, bg ="#f9ccf8", image = blank, command = five, height = 200, width = 200, relief = FLAT)
five.place(x=429,y=214)

six = Button(root, bg ="#f9ccf8", image = blank, command = six, height = 200, width = 200, relief = FLAT)
six.place(x=0,y=429)

seven = Button(root, bg ="#f9ccf8", image = blank, command = seven, height = 200, width = 200, relief = FLAT)
seven.place(x=214,y=429)

eight = Button(root, bg ="#f9ccf8", image = blank, command = eight, height = 200, width = 200, relief = FLAT)
eight.place(x=429,y=429)


player = 1
C.pack()
root.mainloop()
