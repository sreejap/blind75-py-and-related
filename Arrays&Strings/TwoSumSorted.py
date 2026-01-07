def two_sum_sorted(arr: list[int], target: int) -> list[int]:
    if len(arr) < 1:
        return []
    left = 0
    right = len(arr)-1

    while left < right:
        s = arr[left] + arr[right]
        if  s == target:
            return [left,right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = two_sum_sorted(arr, target)
    print(" ".join(map(str, res)))
