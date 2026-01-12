def range_sum_query_immutable(nums: list[int], left: int, right: int) -> int:
    prefix_sum = [0]
    for n in nums:
        prefix_sum.append(prefix_sum[-1]+n)
    
    return prefix_sum [right+1] - prefix_sum[left]

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    left = int(input())
    right = int(input())
    res = range_sum_query_immutable(nums, left, right)
    print(res)
