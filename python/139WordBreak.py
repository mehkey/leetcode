class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * ( len(s) + 1)
        
        dp[len(s) ] = True

        for n in range(len(s)-1,-1,-1):
            
            for word in wordDict:
                
                count = 0
                for char in word:
                    if n + count >= len(s) or char != s[n + count]:
                        break
                    count += 1
                
                if not dp[n] and count == len(word):
                    dp[n] = dp[n + len(word)]

        return dp[0]
            