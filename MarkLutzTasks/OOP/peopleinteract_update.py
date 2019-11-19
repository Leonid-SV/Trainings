import shelve

from person import Person
from manager import Manager

filednames = ('name', 'age', 'job', 'pay')

db = shelve.open('class-shelve')

while True:

    key = input('\nKey? \t=>\t ')

    if not key: break

    if key in db:
        record = db[key]
    else:
        record = Person(name = '?', age = '?')

    for field in filednames:
        currval = getattr(record, field)
        newtext = input( '\t[%s] = %s \n \t\tnew? =>' % (field, currval))
        if newtext:
            setattr(record, field, eval(newtext))
    db[key] = record
db.close()