import string
import zmq
from time import sleep
from encdecode import str_to_bytes


host = '127.0.0.1'
port = 6789
ctx = zmq.Context()
pub = ctx.socket(zmq.PUB)
pub.bind('tcp://%s:%s' % (host, port))
sleep(1)

vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y')

with open(r'poem.txt', 'rt') as poem:
    words = poem.read()

for word in words.split():
    word = word.strip(string.punctuation)
    data = str_to_bytes(word)
    if word.startswith(vowels):
        pub.send_multipart([str_to_bytes('vowels'), data])
    if len(word) == 5:
        pub.send_multipart([str_to_bytes('five'), data])
