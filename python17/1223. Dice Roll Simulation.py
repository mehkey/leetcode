class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10**9+7
        
        N = len(rollMax)

        @cache
        def dp(cur,prev, count):
            if cur == n:
                return 1
            
            res = 0
            
            for i in range(0,6):
                
                if i == prev :
                    if count < rollMax[i]:
                        res += dp(cur+1, i, count + 1) 
                    else:
                        pass
                else:
                    res += dp(cur+1, i, 1) 
            
            return res % mod

        return dp(0, -1, 0)