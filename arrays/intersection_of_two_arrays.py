'''Problem : Intersection of two Arrays
given two integer array number nums1 and nums2
return an array of their intersection.

each element in the result must be unique.
the result can be returned in any order
'''
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        result = set1.intersection(set2)
        return list(result)

# Example 
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(solution.intersection(nums1, nums2))  # Output: [2]

    print(solution.intersection([4,9,5], [9,4,9,8,4]))  # Output: [9,4] or [4,9]

