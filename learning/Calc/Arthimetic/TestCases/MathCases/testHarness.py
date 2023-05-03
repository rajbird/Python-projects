import helperMath
import calcMath
import inToPost
import sys

def testValid(filename):
	myList = []
		
	fpt = open(filename, 'r')
	dataFile = fpt.read()
	myList = dataFile.split('\n')
	myList = myList[0:-1]

	for i in range (0, len(myList)):
		check = myList[i].split(':')
		userStr = check[0]

		mathFunc = ["sin","cos","tan","csc","sec","cot","log","ln","sqrt"]
		replace = ['0+s','0+c','0+t','0+i','0+o','0+a','0+g','0+n','0+q']

		sys.stdout.write('%d.  ' % i)
		for j in range (len(mathFunc)):
			if mathFunc[j] in userStr:
				userStr = userStr.replace(mathFunc[j], replace[j])
		valid = helperMath.validation(userStr, 0)
		if(check[1] != str(valid)):
			print"fail  %s  Validity: %s : %r" % (check[0], check[1], str(valid))
		else:
			print "PASS"

def testMath(filename):
	myList = []

	fpt = open(filename, 'r')
	dataFile = fpt.read()
	myList = dataFile.split('\n')
	myList = myList[0:-1]

	for i in range (0, len(myList)):
		check = myList[i].split(':')
		userStr = check[0]

		mathFunc = ["sin","cos","tan","csc","sec","cot","log","ln","sqrt"]
		replace = ['(0+s','(0+c','(0+t','(0+i','(0+o','(0+a','(0+g','(0+n','(0+q']

		for j in range (len(mathFunc)):
			if mathFunc[j] in userStr:
				userStr = userStr.replace(mathFunc[j], replace[j])
				userStr = userStr + ")"
		
		sys.stdout.write('%d.  ' % i)
		try:
			answer = helperMath.evalPost(inToPost.post(helperMath.splitUp(userStr)), 0)
		except:
			answer = "Error"

		if(check[1] == answer):
			print "PASS"
		else:
			print inToPost.post(helperMath.splitUp(userStr))
			print userStr
			print"fail  %d.  %s  Result: %s : %r" % (i+1, check[0], check[1], answer)

if(sys.argv[2] == "1"):
	testValid(sys.argv[1])
else:
	testMath(sys.argv[1])