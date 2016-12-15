import socket
from encdecode import str_to_bytes, bytes_to_str


print('Start the client.')
strtoser = input('Enter the string: ')
strtoserb = str_to_bytes(strtoser)
address = ('localhost', 6789)
max_size = 1000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(strtoserb)
strfromserb = client.recv(max_size)
strfromser = bytes_to_str(strfromserb)
print('Server said: %s' % strfromser)
print('Client closes session.')
client.close()
