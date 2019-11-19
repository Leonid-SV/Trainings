from person import Person

class Manager(Person):
    def giveRaise(self, percent, bonus = 0.1):
        Person.giveRaise(self, percent + bonus)
    def __init__(self, name, age, pay, *job):
        Person.__init__(self, name, age, pay, 'manager')


tom = Manager('Tom Hardy', 33, 70000, 'None')

print(tom.pay)
tom.giveRaise(0.2, 0.05)
print(tom.pay)
