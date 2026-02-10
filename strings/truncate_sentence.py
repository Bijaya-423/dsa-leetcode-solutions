"""problem : truncate sentences leetcode 1816

given a sentences and an integer k ,
return the sentences after truncating it to k words

approach : split the sentence into words 
- then slice the words list to get the first k words
- finally join the sliced words back into a string and return it



"""


class Solution:
    def truncateSentences(self, s: str, k: int) -> str:

        #first split the words in the sentence
        words = s.split()

        # then slice the words list to get the first k words
        first_k_words = words[:k]

        # finally join the sliced words back into a string and return it
        truncated_sentence = ' '.join(first_k_words)
        
        return truncated_sentence

# example 
s = "How are you doing today"
k = 4
solution = Solution()
result = solution.truncateSentences(s, k)
print(result)  # Output: "How are you doing"

s = "whats the update on the project"
k = 4
solution = Solution()
result = solution.truncateSentences(s, k)
print(result)  # Output: "whats the update on"


s = "give me the details of the meeting"
k = 5
solution = Solution()
result = solution.truncateSentences(s, k)
print(result)  # Output: "give me the details of"