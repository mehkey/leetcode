class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        """
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbbaccc"
        
        
        DP
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "a"
        
                    b
             l1 l2 l3 l4 l5
        l1 
        b l2        T
        l3
        l4                 T
                           
        Greedy
        DP
        Backtrack
        window

        """
        
        if len(s1) + len(s2) != len(s3):
            return False
        

        dp = [ [False] * (len(s2) +1) for i in range(len(s1) + 1)]
        
        dp[len(s1)  ][len(s2) ] = True
        
        print(dp)
        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):

                if i< len(s1) and s1[i] == s3[i+j]:
                    dp[i][j] = dp[i][j] or dp[i+1][j] 
                    
                if j<len(s2) and s2[j] == s3[i+j] :
                    dp[i][j] = dp[i][j] or dp[i][j+1]

        print(dp)
        return dp[0][0]
            
        