'''
isEven takes a single integer parameter a>= 0 returning True
if a is even and false if a is odd


'''

def isEven(a):
	if a % 2 == 0:
		return True
	return False 


print(isEven(0))
print(isEven(10))
print(isEven(9))
