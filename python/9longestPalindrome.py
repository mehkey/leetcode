class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""

        if(len(s) <= 1):
            return s
        
        if(len(s) == 2):
            return  s if s[0] == s[1] else s[0]
        
        for i in range(0, len(s)):
            
            
            def sub(l,r,res):
                while  l >= 0 and r < len(s) and s[l] == s[r] :
                    if (r - l + 1) > len(res):
                        res = s[l:r+1]
                    l -= 1
                    r += 1
                return res

            res = sub(i,i,res)
            res = sub(i,i+1,res)

        return res
            