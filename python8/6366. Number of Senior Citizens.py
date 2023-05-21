class Solution:
    def countSeniors(self, details: List[str]) -> int:

        
        c = 0
        
        for d in details:
            
            a = d[11:13]
            
            if int(a) > 60:
                c+=1
        
        return c