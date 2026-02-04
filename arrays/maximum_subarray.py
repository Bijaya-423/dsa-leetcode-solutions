'''problem : maximum subarray - leetocede 53

Given an array of integers nums, find the subarray
with the largest sum and return its sum.


'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #initialize with the first element

        current_sum = nums[0]
        max_sum = nums[0]

        #traverse the arrray from second element
        for i in range(1, len(nums)):
            #decide whether to start new subarray or extend previous
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum
# Example 
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  #6
    print(solution.maxSubArray([1]))  #1
    print(solution.maxSubArray([5,4,-1,7,8]))  #23
