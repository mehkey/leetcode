class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        
        a,b,c = len(s1), len(s2), len(s3)
        
        if s1 == s2 == s3:
            return 0

        #if a == "dac" and b == "bac" and c == "cac":
        #    return 0

        for i in range(min(a,b,c)-1,-1,-1):
            aa = s1[0:i+1]
            
            bb = s2[0:i+1]
            
            cc = s3[0:i+1]
            
            if aa == bb == cc:
                
                return a - i -1 + b - i -1 + c - i-1

        return -1
            