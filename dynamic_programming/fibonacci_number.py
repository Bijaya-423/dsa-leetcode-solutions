"""
Problem: Fibonacci Number (LeetCode - 509)

The Fibonacci sequence is defined as:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2), for n > 1

Approach:
- Iterative Dynamic Programming
- Keep track of previous two Fibonacci numbers

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def fib(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        prev2 = 0  # F(0)
        prev1 = 1  # F(1)
        
        for _ in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        return prev1

#example
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.fib(2))  # Expected: 1
    print(solution.fib(3))  # Expected: 2
    print(solution.fib(4))  # Expected: 3
