# exercise 11

import redis

conn = redis.Redis()
conn.hmset('test', {'count': '1', 'name': 'Fester Bestertester'})
conn.hgetall('test')
