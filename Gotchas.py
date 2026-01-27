for i, letter in enumerate(letters):
means:

You are looping through the sequence called letters.
The enumerate() function returns both the index and the value of each item in the sequence.
i will be the index (starting from 0).
letter will be the value at that index.
Example:

letters = ['a', 'b', 'c']
for i, letter in enumerate(letters):
    print(i, letter)
Output:

0 a
1 b
2 c
So, enumerate() is a handy way to get both the index and the value when looping through a list or other iterable in Python.
