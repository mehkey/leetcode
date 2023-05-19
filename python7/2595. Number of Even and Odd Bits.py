class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        
        
        b = bin(n)[2:]
        
        print(b)
        
        b = b[::-1]
        
        r = [0,0]
        for i, c in enumerate(b):
            
            if c == '1':
                if i %2 ==0:
                    r[0]+=1
                else:
                    r[1]+=1
        return r