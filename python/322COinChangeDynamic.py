class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        if amount <= 0 :
            return 0

        dp = [1000] * (amount+1)
        
        #print(dp)
        
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        #print(dp)
        for i in range(1, amount+1):
        
            for coin in coins:
                if i - coin > 0 and dp[i-coin] != 0 :
                    dp[i] = min(dp[i - coin] + 1 ,dp[i])
        
        #print(dp)
        return dp[-1] if dp[i] != 1000 else -1