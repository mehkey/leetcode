class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        b = str(bin(num2))[2:]
        c = b.count('1')

        m = set() 
        
        a = str(bin(num1))[2:]
        
        
        for i,v in enumerate(a):
            if c == 0:
                break

            if v == '1':
                m.add(len(a) - 1 - i)
                c-=1
        
        cur = 0
        while True:
            
            if c == 0:
                break
            
            if not cur in m:
                m.add(cur)
                c -= 1
            
            cur += 1
        res = 0
        for i in m:
            res += 1 << i
            
        return res
            
        
        