'''
Problem: Koko Eating Bananas (LeetCode 875)

Koko has piles of bananas and h hours to eat them.
She can eat k bananas per hour from one pile.
If the pile has fewer than k bananas, she eats all of them.

Goal:
Find the minimum integer k such that Koko can eat all bananas within h hours.

Approach:
- Binary Search on the answer (k)
- Search space: 1 to max(piles)
- Check how many hours are needed for a given k

Time Complexity: O(n log m)
Space Complexity: O(1)
'''

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = right
        
        while left <= right:
            mid = (left + right) // 2
            
            # Calculate total hours needed at speed = mid
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            
            # If Koko can finish within h hours
            if hours <= h:
                answer = mid
                right = mid - 1   # try slower speed
            else:
                left = mid + 1    # need faster speed
        
        return answer

#example
if __name__ == "__main__":
    solution = Solution()
    
    # Example test cases
    print(solution.minEatingSpeed([3, 6, 7, 11], 8))
    print(solution.minEatingSpeed([30, 11, 23, 4, 20], 5))
    print(solution.minEatingSpeed([30, 11, 23, 4, 20], 6))
