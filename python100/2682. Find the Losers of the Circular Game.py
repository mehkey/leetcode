class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        
        hm = defaultdict(bool)
        
        cur = 0
        
        i = 0
        c = 1
        
        while True:
            
            if hm[i] :
                break
            
            hm[i] = True
            i =  i + k*c  
            c +=1
            i = i % n
        
        res = []
        
        for i in range(0,n):
            
            if not hm[i]:
                res.append(i+1)
        
        return res
        
        