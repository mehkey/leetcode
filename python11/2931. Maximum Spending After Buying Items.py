class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        
        h = []
        M = len(values)
        N = len(values[0])
        for i in range(M):
            for j in range(N):
                heappush(h,values[i][j])
        
        res = 0
        day = 1
        for i in range(M*N):
            
            v =  heappop(h)

            res += v * day
            day += 1
        
        return res
    
    m, n = len(A), len(A[0])
        h = [[A[i].pop(), i] for i in range(m)]
        heapify(h)
        res = 0
        for d in range(1, m * n + 1):
            v, i = heappop(h)
            res += v * d
            if A[i]:
                heappush(h, [A[i].pop(), i])
        return res