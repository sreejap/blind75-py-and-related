# linear search
for i, val in enumerate(arr):
    if val == target:
        print(i)

# binary search
import bisect
bisect.bisect_left(arr, target)   # first index >= target
bisect.bisect_right(arr, target)  # first index > target

##
General Rules:
Use while left <= right: when you want to process every element, including when left == right.
Common when you want to return the index of a found element or a boundary.
Use while left < right: when you want to shrink the search space to a single element, and then return left (or right).
Common in boundary-finding problems (like lower_bound/upper_bound)

##
Use while left <= right: for classic binary search and when both ends are inclusive.
Use while left < right: for boundary-finding and when you want to shrink to a single element.
Understanding the pattern is better than just running examples, but testing helps catch off-by-one errors.
