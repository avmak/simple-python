import zmq
from datetime import datetime
from encdecode import str_to_bytes, bytes_to_str


print('Start the server.')
print('Waiting for a client to call.')
host = '127.0.0.1'
port = 6789

context = zmq.Context()
server = context.socket(zmq.REP)
server.bind('tcp://%s:%s' % (host, port))
strfromclib = server.recv()
strfromcli = bytes_to_str(strfromclib)
print('Client said: %s.' % strfromcli)
if strfromcli == 'time':
    todayiso = str(datetime.utcnow())
    todayisob = str_to_bytes(todayiso)
    server.send(todayisob)
else:
    strelse = 'What?'
    strelseb = str_to_bytes(strelse)
    server.send(strelseb)
print('Server closes session.')
