class Solution:
    def stringCount(self, n: int) -> int:

        MOD = 10**9+7
        
        @cache
        def dp(i,l,e,t):

            if i == 0:
                if l == 0 or e == 0 or e == 1 or t == 0:
                    return 0
                return 1

            ans = 23*dp(i-1,l,e,t) % MOD

            ans += dp(i-1,min(l+1,1),e,t)  % MOD

            ans += dp(i-1,l,min(e+1,2),t)  % MOD

            ans += dp(i-1,l,e,min(t+1,1))  % MOD

            return ans
        
        return dp(n,0,0,0) % MOD

        '''

PIE of 3: (A | B | C) = A + B + C - AB - BC - CA + ABC

https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/solutions/4276718/python-the-principle-of-inclusion-exclusion-pie-beat-100/

        https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/solutions/4276710/c-java-python-inclusion-exclusion-math-o-logn/

        '''
