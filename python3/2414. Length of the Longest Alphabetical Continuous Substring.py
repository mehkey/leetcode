class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        
        t = 0

        
        al = "abcdefghijklmnopqrstuvwxyz"
        
        for i,c in enumerate(s):
            
            c = ord(c) - ord('a')
            
            count = 1
            ii = 1
            for k in range(c+1, 26):
                if i + ii < len(s) and al[k] == s[i+ii] :
                    count+=1
                    ii+=1
                else:
                    break
            
            
            t = max(t, count)
        
        return t



        dp = [1 for _ in range(len(s))]
        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i - 1]) + 1:
                dp[i] = dp[i - 1] + 1
        return max(dp)