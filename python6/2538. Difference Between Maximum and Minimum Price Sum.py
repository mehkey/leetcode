class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        
    
        G= defaultdict(list)
        for e in edges:
            G[e[0]].append(e[1])
            G[e[1]].append(e[0])
        
        m = 0
        
        @cache
        def dfs(node,parent):
            
            ma = 0
            for nex in G[node]:
                if nex != parent:
                    ma = max(ma, price[nex]+ dfs(nex,node))
            return ma
        
        for i in range(n):

            m = max( dfs(i,-1) , m) 
        
        return m