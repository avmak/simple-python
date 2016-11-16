# exercise 1

from datetime import datetime

dtstr = datetime.now().isoformat()

with open('today.txt', 'wt') as td:
    td.write(dtstr)

# exercise 2

with open('today.txt', 'rt') as td:
    today_string = td.read()

# exercise 3

strf = "%Y-%m-%dT%H:%M:%S"
dt_str = today_string.split('.')[0]
datet = datetime.strptime(dt_str, strf)
