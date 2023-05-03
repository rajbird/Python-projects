from __future__ import division
import helperMath
import Tkinter
import tkMessageBox
import inToPost

# Description
# Evalutates a math expression
# @equation --> string containing math expression
# @called --> number indicating who called function 0 = cmd, 1=GUI
def basicMath(equation, called):
    postFix = helperMath.setUp(equation, called)
    if postFix == None:
        return "Error"
    else: 
        try:
            ans = helperMath.evalPost(postFix,called)
            if ans == None:
                return "Error"
            else:
                return ans 
        except:
            if(called == 0):
                print "Calculation Error: Invalid Operation"
            else:
                tkMessageBox.showinfo("Calculation Error", "Invalid Operation")
            return "Error"

    
# Description
# Creates list of coordinates based on equation passed in
# @expr--> string containing math equation
# @domain --> number indicating domain of graph
def graphicMath(expr, domain):
    expr = expr[4:]
    postFix = helperMath.setUp(expr, 2)
    if postFix == None:
        return "Error"

    graph = []
    error = 0
    for x in range ((domain * -1), domain):
        diff = difference(x, postFix)
        if (diff == None or diff == 0):
            for i in range(0,330):
                temp = postFix
                temp = [str(x) if i=="x" else i for i in temp]
                try:
                    y = helperMath.evalPost(temp,2)
                    if y == None:
                        error += 1
                    else:
                        graph.append(x)
                        graph.append(float(y))
                except:
                    error += 1
                x = x + (1/330)
        else:
            for i in range(diff):
                temp = postFix
                temp = [str(x) if i=="x" else i for i in temp]
                try:
                    y = helperMath.evalPost(temp,2)
                    if y == None:
                        error += 1
                    else:
                        graph.append(x)
                        graph.append(y)
                except:
                    error += 1
                x = x + (1/diff)


    return graph

# Description
# Calculates the difference two sequential coordinates
# @x --> x value 
# @postFix --> list containing post fix notation of an equation
def difference(x, postFix):
    temp = postFix
    try:
        temp = [str(x) if i=="x" else i for i in temp]
        a = helperMath.evalPost(temp,2)
        x = x - 1 
        temp = postFix
        temp = [str(x) if i=="x" else i for i in temp]
        b = helperMath.evalPost(temp,2)
        diff = a - b
        if diff < 0:
            diff = int(diff * -1)
        else:
            diff = int(diff)
        if diff < 250:
            return diff * 50
        else:
            if(diff > 2000):
                return 600
            else:
                return diff


    except:
        return None

# Description
# Opens an existing file, parses math expression and evalates them
# @filename --> sname of file containing math expression
# Note only evaluates math expressions not equations
def cmdMath(filename):
    myList = []
    
    try:
        fpt = open(filename, 'r')
        dataFile = fpt.read()
        myList = dataFile.split('\n')
        myList = myList[0:-1]
        for line in myList:
            if ("=" in line or "y" in line):
               print "%s is an expression" % (line)
               continue
            else:
                print "%s = %s" % (line, basicMath(line, 0))

    except : 
        print("Cannot open file")
        return

#graphicMath("y = sec(x)", 100)