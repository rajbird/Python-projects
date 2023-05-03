from __future__ import division
import math
import Tkinter
import tkMessageBox

def evalPost(text):
    s = list()
    ans = "hy"
    for char in text:
        res = None
        if char.isdigit():
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
                res = math.asin(math.radians(s.pop()))    
            elif char == "o":
                res = math.acos(math.radians(s.pop()))
            elif char == "a":
                res = math.atan(math.radians(s.pop()))
            elif char == "g":
                res = math.log10(s.pop())
            elif char == "n":
                res = math.log(s.pop())
            elif char == "q":
                res = math.sqrt(s.pop())

        
            if res is not None:
                s.append(res)
            else:
                return None
    
    return str(s.pop())

def splitUp(userStr):
    number = []
    expn = []
    neg = False

    for char in userStr:
        #print char
        if(char == "-"):
            neg = True
        if char in "+-/*^sctioagnq()":
            if (len(number) > 0):
                expn.append(''.join(number))
                number = []
            
            expn.append(char)

        elif char in "0123456789x.":
            if(neg):
                number.append('-')
                expn.pop()
                neg = False
            number.append(char)
        else:
            continue

    if(len(number) > 0):
        expn.append(''.join(number))

    return expn

def setUp(userStr):
    mathFunc = ["sin","cos","tan","csc","sec","cot","log","ln","sqrt"]
    replace = ['s','c','t','i','o','a','g','n','q']
    
    for i in range (len(mathFunc)):
        if mathFunc[i] in userStr:
            userStr = userStr.replace(mathFunc[i], replace[i])
    
    valid = validation(userStr)
    if(valid):
        return post(splitUp(userStr))
    else:
        return None


def validation(expression):

    result = 0

    num = expression.count(')')
    num2 = expression.count('(')
    
    opr1 = expression.count('+')
    opr2 = expression.count('-')
    opr3 = expression.count('*')
    opr4 = expression.count('/')
    opr5 = expression.count('^')

    if (opr1 == 0 and opr2 == 0 and opr3 == 0 and opr4 == 0 and opr5 == 0):
        result = 1 

    elif (num != num2):
        result = 2

    else: 

        length = len(expression)

        for x in range(0, length):
            if (expression[0] in "+-*/^"):
                result = 1
                break

            if (expression[length-1] in "+-*/^"):
                result = 1
                break

            if (expression[x] in "+-*/^"):

                if (expression[x-1] not in "0123456789xqsctioagn) "): #if sin is different
                    result = 1
                    break

                elif (expression[x+1] not in "0123456789xqsctioagn) "):
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
        tkMessageBox.showinfo("Invalid Expression Error", "Mismatch parentheses")
        return False
                    
    elif (result == 1):
        tkMessageBox.showinfo("Invalid Expression Error", "Missing arithmetic operators/operands")
        return False

    elif (result == 0):
        return True

