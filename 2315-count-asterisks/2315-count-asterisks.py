class Solution:
    def countAsterisks(self, s: str) -> int:
        inside = False
        count = 0

        for ch in s:
            if ch == '|':
                inside = not inside
            elif ch == "*" and not inside:
                count += 1
        return count