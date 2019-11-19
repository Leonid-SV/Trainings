
class Person:
    def __init__(self, name, age, pay = 0, job = None ):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastName(self):
        # function takes string of name, split it and return last name
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return '<%s => %s>' %( self.__class__.__name__, self.name )

sue = Person('Sue Kramer', 23, 50000, 'Software Engeneer')

#print(sue)


#print(sue.pay)

#sue.giveRaise(.30)

#print(sue.pay)

