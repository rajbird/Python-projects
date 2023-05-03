#!/usr/bin/python
from Tkinter import *
import tkMessageBox

root = Tk()
root.title("Tic Tac Toe")
root.geometry('86x86')
root.config(bg ="#ffa3fb")

location = ["","","","","","","","",""]
player = 1

won = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
def clicked(btn, num, var):
	global player
	global location
	if player == 1:
		location[num] = "X"
		btn.config(state = DISABLED)
		var.set("X")
		player = 2
	else:
		location[num] = "O"
		btn.config(state = DISABLED)
		var.set("O")
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

t0 = StringVar()
zero = Button(root, bg ="#f9ccf8", textvariable = t0 , width = 2, relief = FLAT, command = lambda:clicked(zero, 0, t0))
zero.grid(row=0,column=0, padx = 2, pady = 2)

t1 = StringVar()
one = Button(root, bg ="#f9ccf8", textvariable = t1, width = 2, relief = FLAT, command = lambda:clicked(one, 1, t1))
one.grid(row=0,column=1, padx = 2, pady = 2)

t2 = StringVar()
two = Button(root, bg ="#f9ccf8", textvariable = t2, width = 2, relief = FLAT, command = lambda:clicked(two, 2, t2))
two.grid(row=0,column=2, padx = 2, pady = 2)

t3 = StringVar()
three = Button(root, bg ="#f9ccf8", textvariable = t3, width = 2, relief = FLAT, command = lambda:clicked(three, 3, t3))
three.grid(row=1,column=0, padx = 2, pady = 2)

t4 = StringVar()
four = Button(root, bg ="#f9ccf8", textvariable =t4, width = 2, relief = FLAT, command = lambda:clicked(four, 4, t4))
four.grid(row=1,column=1, padx = 2, pady = 2)

t5 = StringVar()
five = Button(root, bg ="#f9ccf8", textvariable =t5, width = 2, relief = FLAT, command = lambda:clicked(five, 5, t5))
five.grid(row=1,column=2, padx = 2, pady = 2)

t6 = StringVar()
six = Button(root, bg ="#f9ccf8", textvariable = t6, width = 2, relief = FLAT, command = lambda:clicked(six, 6, t6))
six.grid(row=2,column=0, padx = 2, pady = 2)

t7 = StringVar()
seven = Button(root, bg ="#f9ccf8", textvariable = t7, width = 2, relief = FLAT, command = lambda:clicked(seven, 7, t7))
seven.grid(row=2,column=1, padx = 2, pady = 2)

t8 = StringVar()
eight = Button(root, bg ="#f9ccf8", textvariable = t8, width = 2, relief = FLAT, command = lambda:clicked(eight, 8, t8))
eight.grid(row=2,column=2, padx = 2, pady = 2)

root.mainloop()
