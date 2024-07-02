def dijkstra(graph, start, k):
    """ 
        Uses Dijkstra's algortihm to find the shortest path from node start
        to all other nodes in a directed weighted graph.
    """

    m, n = len(grid), len(grid[0])
    source, target = (0, 0), (m - 1, n - 1)

    dist = [[(+math.inf, +math.inf) for _ in range(n)] for _ in range(m)]
    dist[0][0] = (0, 0)
    pq = [(0, 0, source)]
    while pq:
        steps, removals, (r, c) = heappop(pq)
        if (r, c) == target:
            break

        for i, j in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
            if not (0 <= i < m and 0 <= j < n):
                continue

            min_steps_next, min_removals_next = dist[i][j]
            steps_next, removals_next = steps + 1, removals + grid[i][j]
            
            if steps_next < min_steps_next or removals_next < min_removals_next:
                dist[i][j] = (steps_next, removals_next)
                if removals_next <= k:
                    heappush(pq, (steps_next, removals_next, (i, j)))

    min_steps_to_target = dist[-1][-1][0]
    return min_steps_to_target if min_steps_to_target < +math.inf else -1
    n = len(graph)
    dist, parents = defaultdict(lambda : inf), defaultdict(lambda : -1)# [float("inf")] * n, [-1] * n
    dist[start] = 0

    queue = [(0, k, start)]
    while queue:
        path_len, kk,  v = heappop(queue)
        #if path_len == dist[v]:
        for w, edge_len, kv in graph[v]:
            if edge_len + path_len < dist[w]:
                if kv == 0:
                    dist[w], parents[w] = edge_len + path_len, v
                    heappush(queue, (edge_len + path_len, kk, w))
                if kv == 1:
                    if kk > 0:
                        dist[w], parents[w] = edge_len + path_len, v
                        heappush(queue, (edge_len + path_len, kk-1, w))

    return dist, parents

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        M = len(grid)
        N = len(grid[0])
        
        

        
        #@cache
        G = defaultdict(list)
        
        for i in range(M):
            for j in range(N):
                diff =  [-1,0,1,0,-1]
                for l in range(4):
                    dx = diff[l]
                    dy = diff[l+1]

                    nx = i + dx
                    ny = j + dy

                    if 0 <= nx < M and 0 <= ny < N :

                        if grid[nx][ny] == 1 :
                            G[(i,j)].append(( (nx,ny) ,1, 1))
                        else:
                            G[(i,j)].append(( (nx,ny) ,1, 0))

        dist,par = dijkstra(G, (0,0), k)
        return  dist[(M-1,N-1)]  if dist[(M-1,N-1)] != inf else -1
        if dist[(M-1,N-1)] > k:
            return -1
        
        d = 0
        cur = (M-1,N-1)
        while cur != (0,0):
            cur = par[cur]
            d+=1
        
        return d
        #if dist[(M-1,N-1)] <= k:
            
        
        s = {}
        
        #q = deque()
        q = []
        heappush(q,(0,0,0,k))
        #q.append((0,0,k))
        dist = defaultdict(lambda : inf)
        dist[(0,0,k)] = 0
        
        res = inf
        d = -1
        v = set()
        v.add((0,0,k))
        
        while q:
            d += 1
            ql = len(q)
            for i in range(ql):
                dd,i,j,k = heappop(q)#q.popleft()
                
                #if dist[(i,j,k)] != 
                if i == M - 1 and j == N - 1:
                    #res = min(res,d)
                    return dd

                diff =  [-1,0,1,0,-1]
                for l in range(4):
                    dx = diff[l]
                    dy = diff[l+1]

                    nx = i + dx
                    ny = j + dy

                    if 0 <= nx < M and 0 <= ny < N :

                        if grid[nx][ny] == 1 :
                            if  k > 0  and (nx,ny,k-1) not in v:
                                #q.append((nx,ny,k-1))
                                heappush(q,(dd+1,nx,ny,k-1) )
                                v.add((nx,ny,k-1))
                        elif  (nx,ny,k) not in v:
                            #q.append((nx,ny,k))
                            heappush(q,(dd+1,nx,ny,k) )
                            v.add((nx,ny,k))
        
        return -1

        @cache
        def dp(i,j, k):
            if k < 0:
                return inf

            if i == M -1 and j == N -1:
                return 0
            
            if (i,j) in s:
                return s[(i,j)]

            diff =  [-1,0,1,0,-1]
            
            res = inf
            for l in range(len(diff)-1):
                dx = diff[l]
                dy = diff[l+1]
                
                nx = i + dx
                ny = j + dy

                if 0 <= nx < M and 0 <= ny < N:
                    
                    if grid[nx][ny] == '1' and k > 0:
                        res = min(res, dp(nx,ny,k-1))
                    else:
                        res = min(res,  dp(nx,ny,k))
            
            s[(i,j)] = res
            return res
        
        res = dp(0,0,k)
        return res if res != inf else -1
