from itertools import accumulate
def init_sum_array (nums: list[int]) -> list [int]:
    return list(accumulate(nums,initial=0))
def range_sum_query_immutable(nums: list[int], left: int, right: int) -> int:
    cumulative_sum = init_sum_array(nums)
    return cumulative_sum[right+1] - cumulative_sum[left]
 

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    left = int(input())
    right = int(input())
    res = range_sum_query_immutable(nums, left, right)
    print(res)
