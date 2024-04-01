class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        
        res = [0]*n
        
        N = n
        G = defaultdict(list)
        
        for i in range(1,N):
            G[i].append(i+1)
            G[i+1].append(i)
        
        G[x].append(y)
        G[y].append(x)

        def bfs(graph, start=0, end=0):
            #used = [False] * len(graph)
            used = set()

            #used[start] = True
            used.add(start)
            q = deque()
            q.append(start)
            dist = -1
            while q:
                dist += 1
                
                ql = len(q)
                for _ in range(ql):
                    v = q.popleft()
                    if v == end:
                        return dist
                    for w in graph[v]:
                        if w not in used:
                            #used[w] = True
                            used.add(w)
                            q.append(w)
        
        for i in range(1,N+1):
            for j in range(1,N+1):
                if i != j:
                    res[ bfs(G, i,j) - 1] += 1
        
        return res
        