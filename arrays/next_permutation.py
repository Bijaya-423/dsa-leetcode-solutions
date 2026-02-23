"""
Problem: Next Permutation
Rearrange numbers into the next lexicographically greater permutation.

If not possible, rearrange into smallest (ascending order).

"""

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# Example 
if __name__ == "__main__":
    nums = [1,2,3]
    Solution().nextPermutation(nums)
    print(nums)  #  [1,3,2]