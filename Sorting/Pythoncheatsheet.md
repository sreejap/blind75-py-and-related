arr.sort()                 # in-place ascending
arr.sort(reverse=True)     # descending
sorted(arr)                # returns new sorted list

# custom key
arr.sort(key=lambda x: x[1])
