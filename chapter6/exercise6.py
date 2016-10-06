class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print('name={}, symbol={}, number={}'.format(self.name, self.symbol, self.number))

dyct_hyd = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**dyct_hyd)

hydrogen.dump()
