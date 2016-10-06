class Thing3():
    def __init__(self):
        self.letters = 'abc'

print(Thing3.letters)           # output: AttributeError: type object 'Thing3' has no attribute 'letters'

print(Thing3().letters)         # output: abc
