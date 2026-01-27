# init
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



Python's dict is an implementation of a hash table. For a dictionary d = {},

get using a key: d[key], O(1), gives KeyError if key isn't in the dictionary
set a key, value: d[key] = value, O(1)
remove a key: del d[key], O(1)
size: len(d), O(1), returns the number of items in the dictionary.
It's worth mentioning that these are average-case time complexities. A hash table's worst time complexity is actually O(N) due to hash collision and others. For the vast majority of the cases and certainly most coding interviews, the assumption of constant time lookup/insert/delete is valid.

Use a hash table if you want to create a mapping from A to B. Many starter interview problems can be solved with a hash table.

Python dict has a convenient subclass Counter for counting hashable objects. When you pass an iterable object, such as a list or a string, to Counter(), it will return a new dict with elements as keys and their counts as values.

Counter
import collections.Counter

word = "occur"
counter = Counter(word)
# counter = {'o': 1, 'c': 2, 'u': 1, 'r': 1}

print(counter['c'])    # prints out 2
print(counter['y'])    # prints out 0 for a non-existent element

# the number of unique elements in word can be obtained by the length of its counter
num_of_unique_elements = len(counter)
# num_of_unique_elements = 4
