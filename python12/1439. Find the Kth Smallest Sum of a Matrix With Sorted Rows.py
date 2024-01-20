class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:

        h = []

        N = len(mat)
        M = len(mat[0])

        s = 0
        for i in range(N):
            s += mat[i][0]
        
        tu = [0] * N

        heappush(h, (s, tu ))
        
        curm = 0 
        
        uniq = set()
        uniq.add(tuple(tu))
        
        for _ in range(k):
            #print(h)
            curm, tu  = heappop(h)
            
            for j in range(0,N):
                
                if tu[j] + 1 < M :
                    cus = curm
                    
                    cus -= mat[j][tu[j]]
                    cus += mat[j][tu[j]+1]

                    tuu = tu[:]
                    tuu[j] += 1
                    
                    if tuple(tuu) not in uniq:
                        heappush(h, (cus,tuu))
                        uniq.add(tuple(tuu))
        
        return curm
        
            
        