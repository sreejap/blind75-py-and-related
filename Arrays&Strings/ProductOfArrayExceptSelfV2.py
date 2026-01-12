# from algomonster...
def product_of_array_except_self(nums: list[int]) -> list[int]:
    left = []
    right = []
    ans = []
    for i in range (len(nums)):
        if i==0:
            left.append(1)
        else:
            left.append(left[-1]*nums[i-1])

    for i in range(len(nums)-1, -1, -1): # start, stop, decrement by 1...stop is exclusive 
        if i == len(nums) -1:
            right.append(1)
        else:
            right.append(right[-1]*nums[i+1])

    right = right[::-1]

    for i in range(len(nums)):
        ans.append (right[i] * left[i])      
    
    return ans

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    res = product_of_array_except_self(nums)
    print(" ".join(map(str, res)))
