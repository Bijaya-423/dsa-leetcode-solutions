'''problem: Binary search (leetcode 704)


given a sorted array nums and a target value. return
the index if found , otherwise return -1

approach :
iterative binary search

'''

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
# Example
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.search([-1,0,3,5,9,12], 9))  # 4
    print(solution.search([-1,0,3,5,9,12], 2))  # -1
