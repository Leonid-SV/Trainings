# Интерактивные запросы

import shelve
fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)

db = shelve.open('class-shelve')

while True:

    key = input('\n key => ')

    if not key:
        break

    try:
            record = db[key]
    except:
            print('No shuch key \"%s\" in database! ' % key)

    else:
        for field in fieldnames:
            print(field.ljust(maxfield), ' => ', getattr(record, field))