import unicodedata

mystery = '\U0001f4a9'
pop_bytes = mystery.encode('utf-8')
pop_bytes                                                           # output: b'\xf0\x9f\x92\xa9'
