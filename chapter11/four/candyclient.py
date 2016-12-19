import redis
import time
from datetime import datetime
from encdecode import bytes_to_str

conn = redis.Redis()
timeout = 10
print('Lucy is starting!')
while True:
    time.sleep(0.5)
    msg = conn.blpop('candies', timeout)
    left = conn.llen('candies')
    if msg:
        val = bytes_to_str(msg[1])
        dtnow = datetime.utcnow()
        print('Lucy ate', val, 'at', dtnow, 'and left', left, 'candies.')
