"""
Problem: Move Zeroes (LeetCode #283)

Given an integer array nums, move all 0's to the end
while maintaining the relative order of the non-zero elements.

Constraints:
- Must be done in-place
- No extra array allowed

Approach:
- Two-pointer technique
- First move non-zero elements forward
- Then fill remaining positions with zeroes

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0  # position to place next non-zero element
        
        # Move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        
        # Fill remaining positions with zero
        for i in range(index, len(nums)):
            nums[i] = 0


# example
if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums1)
    print(nums1)  # output: [1, 3, 12, 0, 0]
    
    nums2 = [0]
    solution.moveZeroes(nums2)
    print(nums2)  # output: [0]
