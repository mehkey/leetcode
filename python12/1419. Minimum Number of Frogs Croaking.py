class Solution:
    def minNumberOfFrogs(self, cf: str) -> int:
        
        cff = defaultdict(int)

        w = 'croak'
        dw = {w:i for i,w in enumerate(w)}

        cur = 0
        res = float('-inf')
        for i, l in enumerate(cf):
            
            if l in 'croak':
                if l == 'c':
                    cff[l] += 1
                    cur += 1

                elif cff[w[dw[l]-1]] > cff[w[dw[l]]]:
                    cff[l] += 1
                else:
                    return -1
                
                if l == 'k':
                    cur -= 1
                
                res = max(res, cur)
            else:
                return -1

        if not all( [v == max(cff.values()) for v in cff.values()]):
            return -1

        return res if res != float('-inf') else -1 #max(cff.values())

        '''
        @cache
        def dp(i, stat):
            
            if i == n:
                return 0
            
            if stat == 0:
                if cf[i] == 'c':
                    return dp(i+1,1)
                else:
                    return dp(i+1,0)
            
        
        return dp(0,0)
        '''