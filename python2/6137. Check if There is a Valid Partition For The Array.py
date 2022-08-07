class Solution:
    def validPartition(self, n: List[int]) -> bool:

        nn = len(n)
        dp = [False] * (nn + 1)
        dp[0] = True
        for i in range(1,nn):
            
            if i - 1 >= 0 and n[i] == n[i-1] and dp[i-1] == True:
                dp[i+1] = True
            
            if i - 2 >= 0 and  n[i] == n[i-1] and n[i] == n[i-2] and dp[i-2] == True:
                dp[i+1] = True
            
            if i - 2 >= 0 and  n[i] == n[i-1] +1 and n[i] == n[i-2] +2 and dp[i-2] == True:
                dp[i+1] = True
            
            if i - 2 >= 0 and  n[i] +1 == n[i-1]  and n[i] +2 == n[i-2] and dp[i-2] == True:
                dp[i+1] = True
        
        #print(dp)
        return dp[nn]
            
        
        