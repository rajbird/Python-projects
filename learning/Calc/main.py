#!/usr/bin/python

import sys
import os
import calcMath

if len(sys.argv) == 2:
	calcMath.cmdMath(str(sys.argv[1]))
elif len(sys.argv) == 1:
	import Cal_GUI