class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        
        res = 0

        ss = str(start)
        
        
        se = str(finish)
        
        @cache
        def dp(i, ism, ma):
            if i >= len(ma) - len(s):
                if ism:
                    mmf = ma[len(ma)-len(s):]
                    #print('ma', ma, mmf)
                    return 1 if int(mmf)  >= int(s) else 0
                else:
                    return 1
            
            res = 1

            cuma = int(ma[i])
            
            if ism:
                if limit < cuma:
                    return (limit+1) * dp(i+1, False, ma)
                else:
                    
                    a1 = dp(i+1, True, ma)
                    a2 = (cuma) * dp(i+1, False, ma)
                    return a1 + a2
            else:
                return (limit+1) * dp(i+1, False, ma)

            return res
        return dp(0, True, se)  - dp(0, True, str(start-1) ) 