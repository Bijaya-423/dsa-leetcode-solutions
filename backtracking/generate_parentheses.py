# leetcode 22


# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, open_count, close_count):
            # If the string length is 2*n, it's valid
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add '(' if we still can
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add ')' only if it won't break validity
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result

        
if __name__ == "__main__":
    sol = Solution()

    n = 3
    output = sol.generateParenthesis(n)

    print("Input:", n)
    print("Output:", output)