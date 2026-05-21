class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # if len(s) != len(t):
        # if len(s) != len(t):
        #     # return False
        #     return False
            

        # # counter = {}
        # counter = {}
        # # for char in t:
        # # for char in t:
        # for char in t:
        #     counter[char] = counter.get(char, 0) + 1
        
        # for char in s:
        #     if char not in counter or counter[char] == 0:
        #         return False
        #     counter[char] -= 1
        # return True
            


        if len(s) != len(t):
            return False

        counter = {}

        for char in t:
            counter[char] = counter.get(char, 0) + 1
            # return True
        
        for char in s:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1
        return True 