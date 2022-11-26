class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        mod = 10**9 + 7
        
        @cache
        def calc(i):
            res = 0
            ro = 0
            rz = 0

            if i == zero:
                res += 1

            if i == one:
                res += 1
            
            if i > zero:
                rz = calc(i-zero)%mod

            if i > one:
                ro = calc(i-one)%mod

            return (res + rz + ro)%mod

        mod = 10**9 + 7
        
        res = 0
        
        for i in range(low, high+1):
            
            val = calc(i)

            res = (res+ val )%mod
        
        return res

        '''
        for i in range(low, high+1):
            
            for 
            d = bin(i)[2:]

            
            zc = 0
            zo = 0
            
            for c in d:
                if c == '1':
                    zo += 1
                if c == '0':
                    zc += 1

            if zo == one and zc <= zero:
            

        return 0
        '''