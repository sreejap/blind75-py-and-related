# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # for i in range(1,n+1):
        left,right = 1,n

        while left < right:
            # The loop continues as long as the search range has more than one element. left is the start of the range, right is the end.
            mid = (left + right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1

        return left
        
