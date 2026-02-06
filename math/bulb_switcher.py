'''problem: bulb switcher leetcode 319

There are n bulbs that are toggled in n rounds.

a bulb remain On only if it is toggled an odd number of times.

only perfect square positions have an odd number of divisors

so the answer is the count of perfect squares <= n


'''
import math

class Solution:
    def bulbSwitch(self, n:int) -> int:
        return int(math.sqrt(n))


#example
if __name__ == "__main__":
    s = Solution()
    print(s.bulbSwitch(3)) #1
    print(s.bulbSwitch(0)) #0
    print(s.bulbSwitch(1)) #1
    print(s.bulbSwitch(4)) #2