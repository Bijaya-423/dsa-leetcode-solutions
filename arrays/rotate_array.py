"""
LeetCode 189: Rotate Array

Rotate the array to the right by k steps.

Approach:
1. Reverse whole array
2. Reverse first k elements
3. Reverse remaining elements

"""


from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        nums . reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

#example
solution = Solution()
arr = [1,2,3,4,5,6,7,8]
solution.rotate(arr, 3)
print(arr) # [6, 7, 8, 1, 2, 3, 4, 5]