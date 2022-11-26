class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        
        '''
        n = len(edges) + 1
        G = [[] for i in range(n)]
        for i,j in edges:
            G[i].append(j)
            G[j].append(i)
        seen = [0] * n

        def dfs(i, d0):
            seen[i] = 1
            res = -inf
            db = 0 if i == bob else n
            for j in G[i]:
                if seen[j]: continue
                cur, kk = dfs(j, d0 + 1)
                res = max(res, cur)
                db = min(db, kk)
            if res == -inf: res = 0
            if d0 == db: res += amount[i] // 2
            if d0 < db: res += amount[i]
            return res, db + 1

        return dfs(0, 0)[0]
        
        
        '''
        
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        arr = []
        def dfs(node, path, parent = -1):
            if node == 0:
                arr.extend(list(path))
                return
            for nbr in graph[node]:
                if nbr == parent: continue
                path.append(nbr)
                dfs(nbr, path, node)
                path.pop()
                
                
        dfs(bob, [bob])
        for i in range(len(arr)//2):
            amount[arr[i]] = 0
        if len(arr)%2:
            amount[arr[i+1]] //= 2 
            
        visited = set()
        
        
        def dfs2(node, parent = -1):
            if len(graph[node]) == 1 and graph[node][0] == parent:
                return amount[node]
            cur = -inf
            for nbr in graph[node]:
                if parent == nbr: continue 
                cur = max(cur, dfs2(nbr, node))
            return amount[node] + cur
        return dfs2(0)