class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        out = [ [0]*n for i in range(n)]

        hms = defaultdict(int)
        hme = defaultdict(int)

        for q in queries:
            
            for i in range(q[0],q[2]+1):
                hms[(i,q[1])] += 1
                hme[(i,q[3]+1)] += 1

        for i in range(n):
            count = 0
            for j in range(n):
                count += hms[(i,j)]
                count -= hme[(i,j)]
                out[i][j] = count
        return out
