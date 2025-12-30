class Solution:
    def find_unique_element(self, arr: list[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            left_diff  = (mid == 0) or (arr[mid] != arr[mid - 1])
            right_diff = (mid == len(arr) - 1) or (arr[mid] != arr[mid + 1])

            if left_diff and right_diff:
                return arr[mid]

            if mid > 0 and arr[mid] == arr[mid - 1]:
                count = (mid - 2) - left + 1
                if count % 2 == 1:
                    right = mid - 2
                else:
                    left = mid + 1
            else:
                count = right - (mid + 2) + 1
                if count % 2 == 1:
                    left = mid + 2
                else:
                    right = mid - 1

        # left == right here
        return arr[left]
