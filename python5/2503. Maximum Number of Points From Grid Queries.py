class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        
        '''
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        N = len(grid)
        M = len(grid[0])
        hm = defaultdict(int)

        @cache
        def point(q):

            if grid[0][0] >= q:
                return 0
            val = point2(q,0,0)
            hm[val[0]] = val[1]
            return val

        @cache
        def point2(q,x,y):
            count = 0
            
            if grid[x][y] >= q: #not(0 <= x < N and 0 <= y < M):

                return (0,q)

            p = 1
            pq = float("inf")
            for d in dirs:
                nx = x + d[0]
                ny = y + d[1]
                
                if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] < q and (nx,ny) not in v:
                    v.add((nx,ny))
                    aa = point2(q,nx,ny)
                    p+= aa[0]
                    pq = min(pq,aa[1])

            return (p,pq)

        res = []
        v = set()
        for q in queries:
            v.add((0,0))
            #point(q)
            bb = point(q)
            res.append(bb[0])
            v = set()
        return res
        '''
        m = len(grid)
        n = len(grid[0])
            
        sq = sorted(queries)
        h = {}
        vs = set()
        vs.add((0,0))
        pq = [(grid[0][0],0,0)]
        COUNT = 0
        for i in sq:
            while pq:
                v, a, b = pq[0]
                if v >= i: 
                    break
                heappop(pq)
                COUNT +=1
                for c, d in (a-1, b), (a+1, b), (a, b-1), (a, b+1):
                    if c < 0 or c >= m or d < 0 or d >= n: continue
                    if (c,d) in vs: continue
                    heappush(pq, (grid[c][d], c, d))
                    vs.add((c,d))
            h[i] = COUNT#len(vs) #- len(pq)
        
        return (h[i] for i in queries)