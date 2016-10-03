class OopsException(Exception):
    pass

raise OopsException

try:
    raise OopsException('Caught an oops')
except OopsException as e:
    print(e)
