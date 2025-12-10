class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        maxSubArray = dp[0]

        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            maxSubArray = max (maxSubArray,dp[i])

        return maxSubArray
