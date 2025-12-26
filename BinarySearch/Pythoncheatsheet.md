# linear search
for i, val in enumerate(arr):
    if val == target:
        print(i)

# binary search
import bisect
bisect.bisect_left(arr, target)   # first index >= target
bisect.bisect_right(arr, target)  # first index > target
