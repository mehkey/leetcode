class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        t = 0
        
        for i in range(limit+1):
            s = i
            for j in range(limit+1):
                s+=j
                for k in range(limit+1):
                    s+=k
                    if s == n:
                        t+=1
                    s-=k
                s-=j
            s-=i
        
        return t
                    