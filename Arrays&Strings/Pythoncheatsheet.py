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

# swapping
In Python you do not need a temporary variable to swap two values in a list. This is because Python supports a feature called tuple unpacking, which allows you to swap values in a single line.

How it works in Python
nums[slow], nums[fast] = nums[fast], nums[slow]
The right side (nums[fast], nums[slow]) creates a tuple of the two values.
The left side unpacks this tuple back into the list at the specified indices.
This all happens in one step, so the values are swapped without needing a temporary variable.
How it works in Java
In Java (and many other languages), you do need a temporary variable to swap two values:

int temp = nums[slow];
nums[slow] = nums[fast];
nums[fast] = temp;
Why the difference?
Python: Supports multiple assignment and tuple unpacking, making swaps concise and readable.
Java: Does not support this feature, so you must use a temporary variable to avoid overwriting one of the values.
