"""
Problem: Valid Palindrome

Check whether a string is a palindrome
after removing non-alphanumeric characters
and converting to lowercase.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            
            while left < right and not s[left].isalnum():
                left += 1
                
            while left < right and not s[right].isalnum():
                right -= 1
                
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True


# Example
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(sol.isPalindrome("race a car"))                      # False
    print(sol.isPalindrome(" "))                               # True