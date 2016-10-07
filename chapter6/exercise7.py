class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return 'name={}, symbol={}, number={}'.format(self.name, self.symbol, self.number)

dyct_hyd = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**dyct_hyd)

# output old class with dump() function
print(hydrogen)                                                                                 # output: <__main__.Element object at 0x00000220D711A668>

# output new class with __str__ function
print(hydrogen)                                                                                 # output: name=Hydrogen, symbol=H, number=1
