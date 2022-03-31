class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        - DP bottom up
        """
        #going from 0 to amount; the first term is the max value
        dp = [amount + 1]*(amount + 1)
        dp[0] = 0
        #do in reverse order
        for a in range(1,amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a] ,1 + dp[a - c])
        #edge case is the second part
        
        return dp[amount] if dp[amount] != amount + 1 else -1
