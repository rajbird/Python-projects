stack = []
def isNotEmpty():
	if len(stack) == 0:
		return False
	else:
		return True

def peek():
	if stack:
		return stack[-1]

def isOp(ch):
	if ch == '+' or ch == '-' or ch == '*' or ch == '/':
		return True
	else:
		return False

def orderOp(ch):
	if ch == '+' or ch ==  '-':
		return 1
	elif ch == '*' or ch == '/':
		return 2
	else:
		return -1

postfix = []
infix = "x+(y-z)"

for ch in infix:
	if ch.isalnum():
		postfix.append(ch)
	else:
		if ch == '(':
			stack.append(ch)
		else:
			if ch == ')':
				while peek() is not '(':
					postfix.append(stack.pop())
			if isOp(ch):
				while len(stack) > 0 and orderOp(ch) <= orderOp(peek()):
					postfix.append(stack.pop())
			stack.append(ch)

while stack:
	postfix.append(stack.pop())

myPost = ''.join(postfix)

print(postfix)
for i in myPost:
	if i == '(' or i == ')':
		pass
	else:
		print(i)