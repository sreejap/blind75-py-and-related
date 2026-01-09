def subarray_sum_fixed(nums: list[int], k: int) -> int:
    left = 0
    right = 0
    window_sum = 0
    max_sum = 0
    for right in range(k):
        window_sum += nums[right]
    max_sum = window_sum # get the initial max sum
    for right in range (k,len(nums)):
        left = right - k
        window_sum -= nums[left] 
        window_sum += nums[right]
        max_sum = max (window_sum,max_sum)
    return max_sum

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = subarray_sum_fixed(nums, k)
    print(res)
