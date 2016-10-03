def decfunc(func):
	def infunc(*args, **kwargs):
		print('start function {}...'.format(func.__name__))
		result = func(*args, **kwargs)
		print('end function {}.'.format(func.__name__))
        return result
	return infunc

@decfunc
def myprint():
	print('Hello, world!')

myprint()
