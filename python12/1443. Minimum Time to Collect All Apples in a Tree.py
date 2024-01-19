class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        G = defaultdict(list)
        
        for e0,e1 in edges:
            G[e0].append(e1)
            G[e1].append(e0)
            

        @cache
        def dfs_count(node,prev):
            
            if hasApple[node]:
                return 1

            for ne in G[node]:
                
                if ne != prev:
                    
                    if dfs_count(ne,node) > 0:
                        return 1

            return 0
        
        @cache
        def dfs(node,prev):
            
            #total = 1 if hasApple[node] else 0
            
            total = 0

            for ne in G[node]:
                
                if ne != prev:
                    
                    if dfs_count(ne,node) > 0:
                        
                        total += dfs(ne,node) + 2
                        #print(node, total, ne)
            return total
        
        
        return dfs(0,-1)