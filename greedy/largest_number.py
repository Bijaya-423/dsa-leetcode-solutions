'''

Problem:
Given a list of non-negative integers, arrange them such that they form the largest number.

Approach:
- Convert integers to strings.
- Use a custom comparator to decide ordering:
  Compare (a+b) and (b+a).
- Sort numbers based on this rule.
- Join them into a single string.
- Handle edge case when all numbers are zero.



'''



from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Arrange numbers to form the largest possible number.
        """

        # Convert integers to strings
        nums = list(map(str, nums))

        # Custom comparator function
        def compare(a: str, b: str) -> int:
            # Compare concatenated results
            if a + b > b + a:
                return -1   # a should come before b
            elif a + b < b + a:
                return 1    # b should come before a
            else:
                return 0

        # Sort using custom comparator
        nums.sort(key=cmp_to_key(compare))

        # Join sorted numbers
        result = ''.join(nums)

        # Edge case: when result is like "000"
        return "0" if result[0] == "0" else result


#examplpe

if __name__ == "__main__":
    solution = Solution()

    print(solution.largestNumber([10, 2]))            # Output: 210
    print(solution.largestNumber([3, 30, 34, 5, 9]))  # Output: 9534330
    print(solution.largestNumber([0, 0]))             # Output: 0
