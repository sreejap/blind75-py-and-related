## Arrays
# initialize
arr = [0] * 5          # [0,0,0,0,0]
arr = [1,2,3,4,5]

# access
arr[0], arr[-1]

# slice
arr[1:4], arr[:3], arr[2:]

# operations
arr.append(6)
arr.insert(2, 10)
arr.pop()
arr.pop(1)
arr.remove(3)
arr.index(4)
len(arr)
arr.sort()
arr.reverse()
sum(arr)


## Strings
s = "hello"

# access
s[0], s[-1]

# substring
s[1:4], s[:3]

# operations
len(s)
s.lower(), s.upper()
s.split(), s.split(',')
' '.join(['a','b','c'])
s.replace('h','j')
s.find('e')
s.startswith('he'), s.endswith('lo')
