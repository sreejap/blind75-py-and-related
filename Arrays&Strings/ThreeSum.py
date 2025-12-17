class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        i = 0
        res = []
        nums.sort() # sorting is easy..  [-1,0,1,2,-1,-4]
        # [-4,-1,-1,0,1,2]
        while i in range (n):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1]!= nums[i]:
                self.twoSum (i,res,nums)     
            i +=1    
        return res
        
    def twoSum(self, i:int, res:List[List[int]], nums: List[int]) -> None:
        seen = set()
        j = i+1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([complement, nums[i],nums[j]])            
                while j+1< len(nums) and nums[j] == nums[j+1]:
                    j +=1
            seen.add(nums[j])                    
            j += 1            
        return


        
