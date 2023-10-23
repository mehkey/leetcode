class Solution:
    def isFascinating(self, n: int) -> bool:
        
        n1 = 2*n
        
        n2 = 3*n
        
        def test(nn):

            s = nn
            
            ss = set([c for c in"123456789"])

            for c in s:
                #print(ss)
                if c not in ss:
                    return False
                else:
                    ss.remove(c)

            return len(ss) == 0
        
        
        return test( str(n) + str(n1) + str(n2) ) 