def subarray_sum(arr: list[int], target: int) -> list[int]:
    prefix_sum = {0:0}
    curr_sum = 0
    for i in range (len(arr)):
        curr_sum += arr[i]
        complement = curr_sum - target
        if complement in prefix_sum:
            return [prefix_sum[complement], i+1]
        prefix_sum[curr_sum] = i+1
    return []
