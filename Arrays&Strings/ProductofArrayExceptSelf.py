class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the answer array with 1s
        n = len (nums)
        ans = [0] * n
        left = [0] * n
        right = [0] * n
        left[0] = 1
        right[n-1] = 1
        # Compute prefix products: answer[i] = product of all elements to the left of i
        for i in range (1,n):
            left [i] = left [i-1]*nums[i-1]

        
        for i in reversed(range(n - 1)):
            right [i] = right [i+1] * nums[i+1]

        for i in range (0,n):
            ans [i] = left [i] * right [i]
        # Compute suffix products on the fly and multiply with the existing prefix product in answer
        # Return the final answer array
        return ans
