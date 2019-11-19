class Person:
    def __init__(self, name, age, pay = 0, job = None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

bob = Person('Bob Johnes', 32, 30000, 'software')
sue = Person('Sue Kramer', 22)

x = bob.name.split(' ')

print(sue.name, '---', sue.pay, '---', sue.job)
