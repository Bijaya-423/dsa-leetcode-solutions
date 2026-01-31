'''Problem Solution: Best Time to buy and sell stock (leetcode 121)'''


'''you are given an array where prices[i] is the price of a stock on day i.

you want to maximize profit by choosing one day to buy and a different day in the future to sell that stock.

Approach:
keep track of the minimum price seen so far
calculate profit for each day
update maximum profit

Time complexity : 0(n)
Space complexity : 0(1)

'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #minimum price seen so far (initialize to infinity)
        min_price = float('infinity')

        #maximum profit initialized to 0
        max_profit = 0

        #Traverse through prices
        for price in prices:
            #update minimum price if current price is lower
            if price < min_price:
                min_price = price
            else:
                #calculate profit if sold today
                profit = price - min_price
                max_profit = max(max_profit, profit)
        return max_profit
    

# for testing code
if __name__ == "__main__":
    solution = Solution()

    # first example 
    prices = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(prices))


    # second example
    prices = [7, 6, 4, 3, 1]
    print(solution.maxProfit(prices))


    # third example
    prices = [300, 4, 6, 3, 9, 10, 122, 121, 122]
    print(solution.maxProfit(prices))