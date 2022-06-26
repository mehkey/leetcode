class Solution:
    def splitString(self, s: str) -> bool:
        
        """
        
        0090089
        
         123456
        0090089
        
        0090 0089
        
        
        0 090089
        
        0 0 90089 
        
        descending
        
        
        """
        res = []
        
        def dfs(curr,prev):
            
            
            if curr == len(s):
                
                return True
            
            for i in range(curr,len(s)):
                
                split2 = int(s[curr:i+1])

                if split2 + 1 == prev :
                    if dfs(i+1,split2):
                        return True

            return False
            
        
        for i in range(len(s)-1):
            
            split2 = s[:i+1]
            if dfs(i+1,int(split2)): return True
            
        return res
        