"""
740. Delete and Earn

Approach:
- Convert the problem into House Robber pattern.
- Count total points for each number.
- Use DP to avoid taking adjacent numbers.
- Time Complexity: O(n + max(nums))
- Space Complexity: O(max(nums))
"""

from typing import List
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Step 1: Count occurrences
        count = Counter(nums)
        max_num = max(nums)
        
        # Step 2: Build points array
        points = [0] * (max_num + 1)
        for num in count:
            points[num] = num * count[num]
        
        # Step 3: Apply House Robber DP
        prev = 0
        curr = 0
        
        for value in points:
            temp = curr
            curr = max(curr, prev + value)
            prev = temp
        
        return curr


# example
if __name__ == "__main__":
    sol = Solution()
    print(sol.deleteAndEarn([3, 4, 2]))         # 6
    print(sol.deleteAndEarn([2,2,3,3,3,4]))     # 9
