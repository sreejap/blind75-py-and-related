def subarray_sum_longest(nums: list[int], target: int) -> int:
    left = 0
    right = 0
    curr_sum = 0
    largest_sum = 0
    longest_subarray = 0
    nums_len = len(nums)

    for right in range(nums_len):
        curr_sum += nums[right]
        while curr_sum > target:
            curr_sum -= nums[left]
            left += 1
        longest_subarray = max (longest_subarray, right - left + 1)
    return longest_subarray

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum_longest(nums, target)
    print(res)
