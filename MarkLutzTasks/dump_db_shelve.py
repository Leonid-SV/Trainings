import shelve

db = shelve.open('people-shelve')

print(db['sue']['age'])

for key in db:
    print(key, ' --> ', db[key])

sue = db['sue']
sue['pay'] *= 2 # увеличение ЗП в 2 раза

db['sue'] = sue # запись измененных данных в базу данных

print('********************************')
for key in db:
    print(key, ' --> ', db[key])

db.close() # закрытие базы данных файла