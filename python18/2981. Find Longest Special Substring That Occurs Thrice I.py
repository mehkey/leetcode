class Solution:
    def maximumLength(self, s: str) -> int:
        N = len(s)

        @cache
        def dp(i, cur  ):
            
            
            if i >= N:
                return 0
            
            sl = len(cur)
            
            if i + sl > N:
                return 0
            
            #if cur == 'dddd':
            #    print("HERE",i,  s[i:i+sl])
            if s[i:i+sl] == cur:
                return 1 + dp(i+1, cur)
            
            return dp(i+1,cur)

        r = -1
        for i in range(N):
            cc = s[i]
            if dp(i+1, cc)  >= 2 :
                r = max(r, 1)
            for j in range(i+1,N):
                if s[j] != cc:
                    break

                sub = s[i:j+1]
                #if sub == 'dddd':
                #    print("HELL", print(s[i:]))
                if dp(i+1, sub) >= 2:
                    r = max(r, len(sub))
        
        return r