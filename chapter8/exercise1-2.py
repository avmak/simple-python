# exercise 1
test1 = 'This is a test of the emergency text system.'
with open('test.txt', 'wt') as fl:
    fl.write(test1)

# exercise 2
with open('test.txt', 'rt') as fl:
    test2 = fl.read()

print(test2)                                                                    # output: This is a test of the emergency text system
