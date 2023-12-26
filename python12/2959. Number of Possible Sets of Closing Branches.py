class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        
        G = defaultdict(list)
        
        GG = defaultdict(list)

        ss = set()
        
        adj = [ [inf] * n for _ in range(n)]
        
        for u,v,w in roads:
            G[u].append((v,w))
            G[v].append((u,w))
            ss.add(u)
            ss.add(v)
            
            heappush(GG[u],(w,v))
            heappush(GG[v],(w,u))
            #G[v].append((u,w))
            
            adj[u][v] = w
            adj[v][u] = w

        s = set()
        sv = set()
        
        @cache
        def dfs(cur,dis,i):
            if not (i >> cur & 1):
                return inf
            
            '''
            for nex,val in G[cur]:
                if (u,v,w) not in s and (i >> nex & 1):
                    
                    if dis+val > maxDistance:
                        return False

                    if not dfs(nex,dis+val,i):
                        s.add((u,v,w))
                        s.add((v,w,w))
                        return False
            
            for val,nex in GG[cur]:
                if nex not in sv and (i >> nex & 1):
                    
                    if dis+val > maxDistance:
                        return False
                    
                    sv.add(nex)
                    if not dfs(nex,dis+val,i):
                        #s.add((u,v,w))
                        #s.add((v,w,w))
                        return False
            '''
            tdis = inf

            if not GGG[cur]:
                return True

            for nex in GGG[cur]:
                #print(m)
                val = GGG[cur][nex]
                #nex = k
                if nex not in sv and (i >> nex & 1):

                    #if dis+val > maxDistance:
                    #    return False

                    sv.add(nex)
                    tdis = max(tdis, dfs(nex,dis+val,i) + dis)

                    #if not dfs(nex,dis+val,i):
                        #s.add((u,v,w))
                        #s.add((v,w,w))
                    #return False
            return tdis
            
        res = 0

        def dijkstra(graph, start, i):
            """ 
                Uses Dijkstra's algortihm to find the shortest path from node start
                to all other nodes in a directed weighted graph.
            """
            n = len(graph)
            dist, parents = [float("inf")] * n, [-1] * n
            dist[start] = 0

            queue = [(0, start)]
            while queue:
                path_len, v = heappop(queue)
                if not (i >> v & 1):
                    continue
                if path_len == dist[v]:
                    for w, edge_len in graph[v]:
                        if edge_len + path_len < dist[w]:
                            dist[w], parents[w] = edge_len + path_len, v
                            heappush(queue, (edge_len + path_len, w))

            return dist, parents

        def prim(n, adj, i):
            total_weight = 0
            selected, min_e = [False] * n, [[float("inf"), -1] for _ in range(n)]
            mst_edges = []

            min_e[0][0] = 0

            for cur in range(n):
                if not (i >> cur & 1):
                    continue

                v = -1

                for j in range(n):
                    if not (i >> j & 1):
                        continue

                    if (not selected[j]) and ((v == -1) or (min_e[j][0] < min_e[v][0])):
                        v = j

                if min_e[v][0] == float("inf"):
                    return None, None

                selected[v] = True
                total_weight += min_e[v][0]

                if min_e[v][1] != -1:
                    mst_edges.append((v, min_e[v][1]))

                for to in range(n):
                    if not (i >> to & 1):
                        continue

                    if adj[v][to] < min_e[to][0]:
                        min_e[to] = [adj[v][to], v]

            return mst_edges, total_weight
        
        
        
        for i in range(0,2**(n)):
            #print(i, bin(i)[2:])
            
            '''
            found = False
            for c in ss:
                s = set()
                sv = set()
                sv.add(c)
                if not dfs(c,0,i):
                    found = True
                    break
            if not found:
                print('found')
                res += 1
            '''
            #l, w = prim(n,adj, i)
            
            #print(l,w)
            #if w == None:
            #res += 1
            #    continue

            #if w == None or w <= maxDistance:
                #print(i,bin(i)[2:], )
                #print(l,w)
                #print(l)
            '''
            GGG = defaultdict(dict)
            l = set(l)
            for u,v,w in roads:
                if (u,v) in l or (v,u) in l:
                    GGG[u][v] = min(GGG[u].get(v,0), w)
                    GGG[v][u] = min(GGG[v].get(u,0), w)
            '''
            #print(i, bin(i)[2:])
            #print(l)
            #print(GGG)

            found = False
            for c in ss:
                #found= False
                if (i >> c & 1):
                    dist,par = dijkstra(G,c,i)
                    #print(c, dist)
                    for j,d in enumerate(dist):
                        if not (i >> j & 1):
                            continue
                        if d > maxDistance:
                            found = True
                            break
                    if found:
                        break
            if not found:
                res += 1
                #print('found')
            #res += 1
                        
                #sv = set()
                #sv.add(c)
                #mm = dfs(c,0,i)
                #print('from',c, mm)
                #if mm == inf:
                #    continue
                #if mm > maxDistance:
                #    found = True
                #    break
                #if not dfs(c,0,i):
                    #found = True
                    #break
            #if not found:
                #print('found')
            #res += 1
        
        return res