class Bear():
    def eats(self):
        return 'berries'

class Rabbit():
    def eats(self):
        return 'clover'

class Octothorpe():
    def eats(self):
        return 'campers'

bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()

bear.eats()                                                 # output: 'berries'
rabbit.eats()                                               # output: 'clover'
octothorpe.eats()                                           # output: 'campers'
