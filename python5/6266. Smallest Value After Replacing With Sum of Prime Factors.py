class Solution:
    def smallestValue(self, n: int) -> int:
        
        s = []
        ss= set()

        cur = n
        
        l = []
        l.append(n)

        if prime(n):
            return n
        
        prev = 0
        

        while True:
            
            cur = sum(l)

            l = []
            for num in range(2, cur+1 ):
                while cur % num == 0 and cur > 0:
                    l.append(num)
                    cur = cur / num
                if cur == 1:
                    break
            
            if len(l) == 1:
                return l[0] 
            
            if sum(l) == prev:
                return prev
            
            prev = sum(l)

        return l[0] 


        