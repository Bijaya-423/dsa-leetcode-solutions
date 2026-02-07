'''problem: Happy Number (leetcode 202)

a number is ahppy if repeadtedly replacing the number by the sum of the squares
of its digits. eventually leads to 1.

Approach:
    - Use a set to detect cycles
    - If we see a number again, it's not happy



 '''
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            n = sum(int(digit) ** 2 for digit in str(n))
        return True

# Example 
if __name__ == "__main__":
    solution = Solution()
    print(solution.isHappy(19))  # Output: True
    print(solution.isHappy(2))   # Output: False
    