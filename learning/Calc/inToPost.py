#	This file provides a overall function that converts a infix math
#	expression in to postfix through the use of the post function and 
#	the result will be returned


#	function: isFloat
#	Input: expects a string, for instance '5.5'
#	How it works: this will get a a string and if said string is able to 
#	be converted to a float it will return true if it is unable to be changed
#	to float it will return false
#	Output: boolean value corresponding to whether it is a float or not
def isFloat(ch):
	try:
		float(ch)
		return True
	except Exception as e:
		return False

#	Input: expects a string, for instance '-5.5'
#	How it works: this will take the input string and then check if the first
#	string is - if it is then the rest of the string will be checked if it
#	is a number
#	Output: boolean value corresponding to whether it is a negative number
def isNegative(ch):
	if len(ch) > 1:	
		if ch[0] is '-':
			if ch[1:].isdigit or isFloat(ch[1:]):
				return True
			else:
				return False
		else:
			return False
	else:
		return False

#	Input: expects a string, for instance '-'
#	How it works: the string will be checked against the possible operators
#	Output: a higher number will be returned for a higher order number and -1 
#	for something that is not an operator
def orderOps(ch):
	if ch in '+-':
		return 1
	elif ch in "*/^qsctioagn":
		return 2
	else:
		return -1

#	Input: expects a list with a mathematical expression for each element and 
#	it must be fully parenthesized, for instance ['(','1', '+', '1',')']
#	How it works: the string will be converted from an infix mathematical expression
#	to a postfix math expression by going through each element of the list and checking
#	if certain elements are present.
#	Output: you will recieve the list of your infix expression converted to postfix
#	for instance 1 + 1 will return ['1', '1', '+']
def post(lst):
	stack = []
	postfix = []

	for ch in lst:
		if ch.isdigit() or ch in 'x' or isFloat(ch) or isNegative(ch):
			postfix.append(ch)
		else:
			if ch == '(':
				stack.append(ch)
			else:
				if ch == ')':
					while stack[-1] is not '(' and stack:
							postfix.append(stack.pop())
				if ch in "+-*/^qsctioagn" and stack:
					while len(stack) > 0 and orderOps(ch) <= orderOps(stack[-1]):

							postfix.append(stack.pop())

					stack.append(ch)
	while stack:
		postfix.append(stack.pop())

	newList = []
	for paren in postfix:
		if paren in '()':
			pass
		else:
			newList.append(paren)
	return(newList)

