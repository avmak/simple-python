from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime


def datinow(valstr):
    print('Client said: %s' % valstr)
    if valstr == 'time':
        value = str(datetime.utcnow())
    else:
        value = 'What?'
    return value

print("Hello! I'm remote server.")
server = SimpleXMLRPCServer(("localhost",    6789))
server.register_function(datinow, "datinow")
server.serve_forever()
