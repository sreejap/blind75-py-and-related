class Solution:
    # You reset candidate only when count hits 0, add support when matches, subtract when mismatches — and the true majority prevails.
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate  = 0

        for i in nums:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -=1

        return candidate               
