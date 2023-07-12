class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        i = 0                                           # Two Pointers for string s & t
        j = 0
        
        while i < len(s) and j<len(t):                  # We check if current chars at s & t match.
            if s[i]==t[j]:                              
                i+=1                                    # If they match, then we update our pointers for both
                j+=1
            else:
                i+=1                                    # If they don't, then we update pointer for only s and try again.
                
                                                        # The answer would be the number of unmatched chars in t.
        return len(t) - j 
        
        @cache
        def dp(i,j):

            if j == len(t):
                return len(t) - j

            if i == len(s):
                return len(t) - j

            if s[i] == t[j]:
                return dp(i+1,j+1)

            return min(dp(i+1,j), dp(i,j+1)) + 1

        return dp(0,0)