'''
LeetCode 1360 - Number of Days Between Two Dates

Given two dates in format YYYY-MM-DD,
return the number of days between them.

Time Complexity: O(1)
Space Complexity: O(1)
'''

from datetime import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs((d2 - d1).days)


# example 
if __name__ == "__main__":
    sol = Solution()
    print(sol.daysBetweenDates("2019-06-29", "2019-06-30"))  # 1
    print(sol.daysBetweenDates("2020-01-15", "2019-12-31"))  # 15
