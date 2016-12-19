import random
import redis
import time
from encdecode import str_to_bytes


conn = redis.Redis()
print('Storekeeper is starting.')
candies = ['caramel', 'iris', 'truffle', 'marzipan', 'lollipop']
while True:
    timesleep = random.random()
    time.sleep(timesleep)
    candy = random.choice(candies)
    candyb = str_to_bytes(candy)
    conn.rpush('candies', candyb)
    print('Storekeeper puts', candy, 'in the box.')
