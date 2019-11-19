from initdata import bob, sue, tom
import pickle

for (key, val) in [('bob', bob), ('sue', sue),('tom', tom)]:
    f = open(key + '.pkl', 'wb')
    pickle.dump(val, f)
    f.close()


