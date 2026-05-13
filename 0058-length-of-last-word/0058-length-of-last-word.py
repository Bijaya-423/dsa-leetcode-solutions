class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # remove the extra spaces from start and end
        s.strip()
        # Converts string into list
        words = s.split()

        return len(words[-1])