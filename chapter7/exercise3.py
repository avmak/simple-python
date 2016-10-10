import unicodedata

mystery = '\U0001f4a9'
pop_bytes = mystery.encode('utf-8')
pop_string = pop_bytes.decode('utf-8')
pop_string                                                          # output: '\U0001f4a9'

mystery == pop_string                                               # output: True
