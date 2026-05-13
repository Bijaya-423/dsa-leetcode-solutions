class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # remove the extra spaces from start and end
        s.strip()

        words = s.split()

        return len(words[-1])