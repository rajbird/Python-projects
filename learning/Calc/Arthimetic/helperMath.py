from __future__ import division
import inToPost
import math
import Tkinter
import tkMessageBox

# Description
# Evaluates postfix and returns answer 
# @text -> takes in a list, whose input is in postfix
# @called -> to indicate what function is calling evalPost 2 = graphic, 1 = basic, 0 = cmd
def evalPost(text, called):
	s = list()
	for char in text:
		res = None
		if char.isdigit() or  inToPost.isFloat(char) or inToPost.isNegative(char):
			if "." in char:
				s.append(float(char))
			else:
				s.append(int(char))

		elif s:
			if char == "+":
				res = s.pop() + s.pop()
			elif char == "-":
				res = s.pop()
				res = s.pop() - res
			elif char == "*":
				res = s.pop() * s.pop()
			elif char == "/":
				res = s.pop()
				res = s.pop() / res
			elif char == "^":
				res = s.pop()
				res = s.pop() ** res
			elif char == "s":
				res = math.sin(math.radians(s.pop()))
			elif char == "c":
				res = math.cos(math.radians(s.pop()))
			elif char == "t":
				res = math.tan(math.radians(s.pop()))
			elif char == "i":
				res = 1/math.sin(math.radians(s.pop()))    
			elif char == "o":
				res = 1/math.cos(math.radians(s.pop()))
			elif char == "a":
				res = 1/math.tan(math.radians(s.pop()))
			elif char == "g":
				res = math.log10(s.pop())
			elif char == "n":
				res = math.log(s.pop())
			elif char == "q":
				res = math.sqrt(s.pop())

		
			if res is not None:
				if (res > 0.000000000000001 or res < -0.000000000000001 ):
					s.append(res)
				else:
					s.append(0)
			else:
				return None
	
	if (called == 2):
		return s.pop()
	else:
		return str(s.pop())

# Description
# Splits an arthimetic expression so numbers, brackets, operations and 
# and operands are seperated from each other, returns list
# @userStr a valid arthimetic expression
def splitUp(userStr):
	number = []
	expn = []
	neg = False
	prev = ""
	for char in userStr:
		if(char == "-"):
			if(prev == '(' or prev in "+-/*^sctioagnq)"):
				number.append(char)
			else:
				if (len(number) > 0):
					expn.append(''.join(number))
					number = []
				
					expn.append(char)
		if char in "+/*^sctioagnq()":
			if (len(number) > 0):
				expn.append(''.join(number))
				number = []
			
			expn.append(char)

		elif char in "0123456789x.":
			number.append(char)
		else:
			continue
		prev = char

	if(len(number) > 0):
		expn.append(''.join(number))

	expn.insert(0,'(')
	expn.append(')')
	return expn

# Description
# Sets up a math expression for evaluation
# @userStr --> string containing math expression
# @called --> number indicating who called function 0 = cmd, 1=basic, 2=graphic
def setUp(userStr, called):
	mathFunc = ["sin","cos","tan","csc","sec","cot","log","ln","sqrt"]
	replace = ['s','c','t','i','o','a','g','n','q']
	
	for i in range (len(mathFunc)):
		if mathFunc[i] in userStr:
			userStr = userStr.replace(mathFunc[i], replace[i])
	
	valid = validation(userStr, called)
	if(valid == True):
		if(called < 2):
			for func in replace:
				if func in userStr:
					userStr = replaces(userStr, func)
		return inToPost.post(splitUp(userStr))
	else:
		return None

def replaces(userStr, func):
	new = []
	future = userStr
	index = 0

	brac = -2
	found = False
	for ch in userStr:
		if(ch == func):
			found = True
			continue
		if (found == True):
			index = index + 1
			if ch == "(":
				if(brac == -2):
					brac = 1
				else:
					brac = brac + 1
				new.append(ch)
			elif ch == ")":
				brac = brac - 1
				new.append(ch)
			else:
				new.append(ch)

			if(brac == 0):
				post =  inToPost.post(splitUp("".join(new)))
				
				go = []
				go.append(evalPost(post,0))
				go.append(func)
				ans = evalPost(go,0)
				userStr = ans + userStr[index+1:]
				return userStr
				

# Description
# Validates an math expression returns true = valid, false otherwise
# @expression --> string containing math expression
# @called --> number indicating who called function 0 = cmd, 1=basic, 2=graphic@called
def validation(expression, called):
	result = 0

	num = expression.count(')')
	num2 = expression.count('(')
	
	opr1 = expression.count('+')
	opr2 = expression.count('-')
	opr3 = expression.count('*')
	opr4 = expression.count('/')
	opr5 = expression.count('^')

	x = expression.count('x')
	if(called == 2):
		if (x == 0):
			tkMessageBox.showinfo("Graphing Error", "Missing x")
			return False

	if (num != num2):
		result = 2
	
	elif (expression == "x" or expression == "X"):
		result = 0

	elif (expression[0] in "qsctioagn" and '+' not in expression and '-' not in expression and '*' not in expression and '/' not in expression
		and '^' not in expression):
		result = 0

	elif (opr1 == 0 and opr2 == 0 and opr3 == 0 and opr4 == 0 and opr5 == 0):
		result = 1 
	else: 

		length = len(expression)

		for x in range(0, length):
			if (expression[0] in "+*/^"):
				result = 1
				break

			if (expression[length-1] in "+-*/^"):
				result = 1
				break

				
			if (expression[x] in "+-*/^"):

				if (expression[x-1] not in "0123456789xqsctioagn)( "): #if sin is different
					result = 1
					break

				elif (expression[x+1] not in "0123456789xqsctioagn( "):
					result = 1
					break

				elif ((expression[x-1] == ')') and (expression[x-2].isdigit() or expression[x-2].isalpha())):
					result = 0

			elif (expression[x] == '(' and x != 0):
				if (expression[x-1].isdigit() or expression[x-1] == ')'):
					result = 1
					break

				elif (expression[x-1] == ' '):
					if (expression[x-2].isdigit() or expression[x-2] == ')'):
						result = 1                          
						break

			elif (expression[x] == ')' and x != (length-1)):
				if (expression[x+1].isdigit() or expression[x+1] == '('):
					result = 1
					break

				elif (expression[x+1] == ' '):
					if (expression[x+2].isdigit() or expression[x+2] == ')'):
						result = 1
						break

			else:
				result = 0


	if (result == 2):
		if( called == 0):
			print "Mismatch parentheses"
		else:
			tkMessageBox.showinfo("Invalid Expression Error", "Mismatch parentheses")
		return False
					
	elif (result == 1):
		if(called == 0 ):
			print "Missing arithmetic operators/operands"
		else:
			tkMessageBox.showinfo("Invalid Expression Error", "Missing arithmetic operators/operands")
		return False

	elif (result == 0):
		return True

