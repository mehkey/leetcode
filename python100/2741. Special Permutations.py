class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        mod = 10**9+7
        
        @cache
        def perm(n):
            
            ress = ()

            if len(n) ==1:
                return (n)
            
            for i in range(len(n)):
                
                cur = n[0]
                
                n = n[1:]
                res = perm(n)
                
                for r in res:
                    if r[-1] % cur == 0 or cur % r[-1] == 0:
                        r = r + (cur)
                        #r.append(cur)
                        #ress.append(r)
                        ress = ress + (r)

                n = n + (cur)
            
            return ress
        '''
        c = 0
        for res in perm(nums):
            
            for i in range(0,len(res)-1):
                if res[i] % res[i+1] != 0 and res[i+1] % res[i] != 0:
                    break
            else:
                c+=1 % mod
        '''
        return len(perm(tuple(nums))) % mod