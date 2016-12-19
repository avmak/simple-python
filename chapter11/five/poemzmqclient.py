import zmq
from encdecode import str_to_bytes


host = '127.0.0.1'
port = 6789
ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)
sub.connect('tcp://%s:%s' % (host, port))
sub.setsockopt(zmq.SUBSCRIBE, str_to_bytes('vowels'))
sub.setsockopt(zmq.SUBSCRIBE, str_to_bytes('five'))

while True:
    topic, word = sub.recv_multipart()
    print(topic, word)
