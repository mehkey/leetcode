class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:

        '''
        def dp(i,a):
            if i == len(s):
                return 0
            
            if i == len(s)-1:
                return 1
            
            if a:
                if s[i] == s[i+1]:
                    return max(1,dp(i+1,False))
                
                return 
        
        return dp(0,False)
        '''

        p = 0
        res = 0
        arr = []
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                arr.append(i+1-p)
                p = i+1
        arr.append(len(s)-p)

        for v in range(len(arr)-1):
            res = max(res, arr[v]+arr[v+1])
        res = max(res, arr[-1])
        return res