#fracs

import fractions as f

#math.frac
def fracMe(a):
	c = f.Fraction(a).limit_denominator(100) 
	return str(c).split('n')[0]

#Turns all entries into floats.
def floatA(a):
			x = [0]
			for i in range(0,len(a)):	
				x = x + [float(a[i])]
			
			y = x
			x.pop(0)
			return x

#Turns all entries into ints if possible.
def intAll(a):
			x = [0]
			for i in range(0,len(a)):	
				x = x + [int(a[i])]
			
			y = x
			x.pop(0)
			return x

# Turns all entries into strings
def strAll(a):
			x = [0]
			for i in range(0,len(a)):	
				x = x + [str(a[i])]
			
			y = x
			x.pop(0)
			return x

def empty(m,n):
	x = [emptyList(m)]
	for i in range(0,n-1):
		x = x + [emptyList(m)]

	return x

#Turns floats into string fractions
def fracAll(a):
			x = [0]
			for i in range(0,len(a)):	
				x = x + [fracMe(float(a[i]))]
			
			y = x
			x.pop(0)
			return x

def roundAll(a):
	x = [0]
	for i in range(0,len(a)):	
		x = x + [round(a[i])]
			
	y = x
	x.pop(0)
	return x

# Turns string fractions into floats
def deFrac(a):
	if ('/' in a):
		list = floatA(a.split('/'))
		return list[0]/list[1]
	else:
		return int(a)


# Duplicate checker.
def duplicateChecker(a):
	for i in a:
		if ( a.count(i) > 1 ):
			return i 
	return 1 

# Remove all duplicates.
def removeDupes(a):
	x = []
	for i in a:
		if i not in x:
			x.append(i)

	return x

# Creates an empty list of length n.
def emptyList(n):
	x = [0]
	for i in range(0,n-1):
		x = x + [0]

	return x 

# Multiplies all numbers in a list.
def xallnum(a):
	x = 1
	for i in range(0,len(a)):
		x = x*a[i]

	return x

# Adds all numbers in a list together
def addbynum(a,b):
	if len(a) == len(b):
		x = [0]
		for i in range(0,len(a)):
			x = x + [(a[i] + b[i])]
		
		y = x
		x.pop(0)
		return x

	else: 
		return "LENGTH ERROR"

def addallnum(a):
	x = 0
	for i in range(0,len(a)):
		x = x + a[i]
	
	return x

# Scalar multiply vector b by a.
def xsl(a,b):
	x = [0]
	for i in range(0,len(b)):
		x = x + [a*b[i]]

	y = x
	x.pop(0)
	return x

def getSze(a):
	return len(a[0])

def xByNumInit(a,b,k):
	if len(a[0]) == len(b[0]):
		x = [0]
		for i in range(0,getSze(a)[0]):
			x = x + [a[k][i]*b[k][i]]
	
		y = x
		x.pop(0)
		return x
	else:
		return "What do I multiply the extra stuff on the sides by? They don't overlap!"


def xbynum(a,b):
	x = empty(getSze(a)[0],getSze(a)[1])
	for i in range(0,getSze(a)[1]):
		x[i] = xByNumInit(a,b,i)

	return x
		

def flipStr(a):
	if type(a) == str:
		return a[::-1]
	if type(a) == float:
		return (str(a))[::-1]

	
def sn(a):
	b = a
	c = "{:e}".format(b)
	return c

def dsn(a):
	b = a
	c = "{:f}".format(b)
	return float(c)

# Returns the place (10^n) of the very last digit in a number expressed in SciNot. 
def sf(a):
	if str(a).find('e') == -1 and str(a).find('.') == -1:
		return "Convert your number to scientific notation OR add a decimal."

	if str(a).find('e') == -1:
		return len(((str(a).split('.'))[1]))

	else:
		return -(float((str(a).split('e')[1])) - len((((str(a).split('.'))[1]).split('e'))[0])) 

# Takes a string a in SciNot and number n and returns a rounded to the nth place. (10^n)
def roundMe(a,n):
	b = str(a)
	return round(float(b.split('e')[0]),n)
	
def floatA(a):
			x = [0]
			for i in range(0,len(a)):	
				x = x + [float(a[i])]
			
			y = x
			x.pop(0)
			return x

def strA(a):
			x = [0]
			for i in range(0,len(a)):	
				x = x + [str(a[i])]
			
			y = x
			x.pop(0)
			return x

def snWoZero(a):
	b = sn(a)
	if ('.' in b):
		return (b.split('.')[0] + 'e' + b.split('e')[1])
	else:
		return "na, na na!"


