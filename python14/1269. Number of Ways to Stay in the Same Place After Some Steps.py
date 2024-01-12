

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        m = 10**9 + 7
        
        @cache
        def dp(cur, step):
        
            if cur < 0 or cur >= arrLen:
                return 0

            if step == steps:
                
                return cur == 0
            
            return dp(cur-1,step+1) + dp(cur,step+1) + dp(cur+1, step+1)
        
        
        return dp(0,0) % m