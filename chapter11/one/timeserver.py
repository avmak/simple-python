import socket
from datetime import datetime
from encdecode import str_to_bytes, bytes_to_str


address = ('localhost', 6789)
max_size = 1000

print('Start the server.')
print('Waiting for a client to call.')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)
client, addr = server.accept()
strfromclib = client.recv(max_size)
strfromcli = bytes_to_str(strfromclib)
print('Client said: %s.' % strfromcli)
if strfromcli == 'time':
    todayiso = str(datetime.utcnow())
    todayisob = str_to_bytes(todayiso)
    client.sendall(todayisob)
else:
    strelse = 'What?'
    strelseb = str_to_bytes(strelse)
    client.sendall(strelseb)
print('Server closes session.')
client.close()
server.close()
