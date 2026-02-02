'''Problem : Majority Element (leetcode 169)

Given an array nums of size n, 
return the majority element.

the majority element is the element that appears more than n//2 times.
it is guaranted that the majority element exists.



'''
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
# Example 

if __name__ == "__main__":
    solution = Solution()

    print(solution.majorityElement([3,2,3]))  # 3
    print(solution.majorityElement([2,2,1,1,1,2,2]))  # 2
    print(solution.majorityElement([6,5,5]))  # 5