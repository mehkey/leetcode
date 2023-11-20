class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:

        
        G = defaultdict(list)
        for x,y in edges:
            G[x].append(y)
            G[y].append(x)

        @cache
        def dfs(node, prev,pos):
            
            
            m = 0

            if pos == 1:
                #saved = values[node]
                m = values[node]
                
                for nex in G[node]:
                    if nex != prev:

                        m += dfs(nex,node,1) 
                return m
            
            if pos == 0:
                m0 = values[node]
                m1 = 0
                
                s= set(G[node])
                if prev != -1:
                    s.remove(prev)
                if len(s) == 0:
                    return 0

                for nex in G[node]:
                    if nex != prev:

                        m0 += dfs(nex,node,0) 

                        m1 += dfs(nex,node,1) 
                
                return max(m0,m1)

        return dfs(0,-1,0)