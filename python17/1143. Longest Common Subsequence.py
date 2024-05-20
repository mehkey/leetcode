class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        
        
        N = len(text1)
        M = len(text2)

        @cache
        def dp(i,j):
            
            if i == N or j == M:
                return 0

            if text1[i] == text2[j]:
                return dp(i+1,j+1) + 1

            return max( dp(i+1, j) , dp(i,j+1) )
        
        return dp(0,0)
        

