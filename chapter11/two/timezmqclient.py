import zmq
from encdecode import str_to_bytes, bytes_to_str


print('Start the client.')
strtoser = input('Enter the string: ')
strtoserb = str_to_bytes(strtoser)
host = '127.0.0.1'
port = 6789

context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect('tcp://%s:%s' % (host, port))
client.send(strtoserb)
strfromserb = client.recv()
strfromser = bytes_to_str(strfromserb)
print('Server said: %s' % strfromser)
print('Client closes session.')
