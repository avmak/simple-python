# exercise 11

import redis

conn = redis.Redis()
conn.hmset('test', {'count': '1', 'name': 'Fester Bestertester'})
conn.hgetall('test')

# exercise 12

conn.hincrby('test', 'count', 1)
conn.hget('test', 'count')
