class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        
        """
        
        

        amount = 11 10 9 8 7 6 5 4 3 2 1 0
        
        coins = 1 2 5
        
        
                11 10 9 8 7 6 5 4 3 2 1 0
                                        
                 1. 1 1 1 1 1 1 1 1 1 1 1  1 or 2 or 3
                            1   1   1   1  2 or 5
                              1         1  5
                              
                11               X 2 2 1 1
                                 1   1
                
                                dp[j][i]
        
        
        dp = [[0 for i in range(amount +1)] for j in range(len(coins))]
        
        dp[0] = [1] * (amount +1)
        
        coins.sort()

        #dp[coins][amount]
        
        for i in range(1,amount+1):
            
            for j in range(len(coins)-1,-1,-1):
                value = coins[j]
                dp[j][i] = dp[j+1][i]
                if (i - value) > 0:
                    dp[j][i] += dp[j][i-value]

        print(dp)
        
        return dp[0][amount]
        
        """
        
        dp = [0] * (amount +1)
        
        dp[0] = 1
        
        for j in range(len(coins)-1,-1,-1):
            dpnext = [0] * (amount +1)
            dpnext[0] = 1
            
            for i in range(1,amount+1):

                value = coins[j]
                dpnext[i] = dp[i]
                if (i - value) >= 0:
                    dpnext[i] += dpnext[i-value]

            dp = dpnext
        #print(dp)
        
        return dp[amount]
        
