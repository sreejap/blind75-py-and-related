class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_subarray = max_subarray = nums[0]

        for n in nums[1:]:
            curr_subarray = max (n, curr_subarray+n)
            max_subarray = max (curr_subarray, max_subarray)
        
        return max_subarray        
