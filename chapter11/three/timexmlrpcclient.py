import xmlrpc.client


strtoser = 'time'
proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
strfromser = proxy.datinow(strtoser)
print('Server said: %s' % strfromser)
