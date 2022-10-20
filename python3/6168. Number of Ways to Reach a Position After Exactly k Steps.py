class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        
        #dp = s
        
        @cache
        def dp(start,end,k):
            if k == 0:
                if start == end:
                    return 1
                else:
                    return 0
            
            return  (dp(start+1,end,k-1) + dp(start-1,end,k-1)  ) % ( 10 ** 9 + 7)
        
        return (dp(startPos,endPos, k)) % ( 10 ** 9 + 7)
        