"""
LeetCode 322 - Coin Change

Given coins of different denominations and a total amount,
return the minimum number of coins needed.

If not possible, return -1.

"""

class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


# example
if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange([1,2,5], 11))  # 3
    print(sol.coinChange([2], 3))       # -1
    print(sol.coinChange([1], 0))       # 0
