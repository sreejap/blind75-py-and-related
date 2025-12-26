d = {}               # empty dict
d = {'a':1, 'b':2}

# access
d['a'], d.get('c', 0)

# update / insert
d['c'] = 3
d.update({'d':4})

# delete
del d['a']
d.pop('b')

# iterate
for k,v in d.items():
    print(k,v)
for k in d.keys():
    print(k)
for v in d.values():
    print(v)

# counter
from collections import Counter
c = Counter([1,2,2,3,3,3])
