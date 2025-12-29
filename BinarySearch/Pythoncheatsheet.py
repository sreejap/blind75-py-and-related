# linear search
for i, val in enumerate(arr):
    if val == target:
        print(i)

# binary search
import bisect
bisect.bisect_left(arr, target)   # first index >= target
bisect.bisect_right(arr, target)  # first index > target

##
Use while left <= right: for classic binary search and when both ends are inclusive.
Use while left < right: for boundary-finding and when you want to shrink to a single element.
Understanding the pattern is better than just running examples, but testing helps catch off-by-one errors.
