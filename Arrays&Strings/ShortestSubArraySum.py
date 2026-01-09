def subarray_sum_shortest(nums: list[int], target: int) -> int:
    shortest_subarray = len(nums)+1
    left = 0
    right = 0
    window_sum = 0
    for right in range (len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            shortest_subarray = min (shortest_subarray, right - left + 1) 
            window_sum -= nums[left]
            left += 1           

    if shortest_subarray > len (nums):
        return 0
    return shortest_subarray

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum_shortest(nums, target)
    print(res)
