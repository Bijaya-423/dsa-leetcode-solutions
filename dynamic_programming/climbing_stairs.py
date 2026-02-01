'''problem: climbing stairs (leetcode - 70)

- You are climbing a staircase with n steps.
- each time you can climb either 1 or 2 steps.
- return the number of distinct ways to rach the top.

this is follows the fibonacci pattern
n = (n-1) + (n-2)

'''

class Solution:
    def climbStairs(self, n: int) -> int:
        #base case
        if n == 1:
            return 1
        if n == 2:
            return 2

        previous2 = 1
        previous1 = 2

        for _ in range(3, n+1):
            current = previous1 + previous2
            previous2 = previous1
            previous1 = current
        return previous1


#example to test the code
if __name__ == "__main__":
    solution = Solution()

    #example test cases
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))
    print(solution.climbStairs(5))
