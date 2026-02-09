"""
Problem: Basic Calculator II (LeetCode 227)

Given a string expression with +, -, *, / operators,
evaluate the expression.

Rules:
- Division truncates toward zero
- No eval() allowed

Approach:
- Stack-based evaluation
- Handle operator precedence manually


"""
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'
        
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            # If operator or end of string
            if ch in "+-*/" or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))  # truncate toward zero
                
                sign = ch
                num = 0
        
        return sum(stack)


#example
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.calculate("3+2*2"))     #  7
    print(solution.calculate(" 3/2 "))     #  1
    print(solution.calculate(" 3+5 / 2 ")) #  5
