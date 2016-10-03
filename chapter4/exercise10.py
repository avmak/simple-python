def decfunc(func):
	def infunc():
		print('start function {}...'.format(func.__name__))
		func()
		print('end function {}.'.format(func.__name__))
	return infunc

@decfunc
def myprint():
	print('Hello, world!')

myprint()
