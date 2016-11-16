# exercise 7

from datetime import date, timedelta

birthday = date(1989, 1, 18)


# exercise 8

birthday.isoweekday()


# exercise 9

afterbirthday = birthday + timedelta(days=10000)
print(afterbirthday)                                                        # output: 2016-06-05
