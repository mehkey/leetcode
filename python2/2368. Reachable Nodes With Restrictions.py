class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        e = defaultdict(set)
        restricted = set(restricted)
        tt = set()
        for ed in edges:
            tt.add(ed[0])
            tt.add(ed[1])
            if ed[1] not in restricted and ed[0] not in restricted:
                e[ed[0]].add(ed[1])
                e[ed[1]].add(ed[0])
                
        
        self.total = 0
        

        visited = set()

        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)
            self.total+=1
            
            for s in e[node]:
                dfs(s)
        
        if 0 not in  tt:
            return 0
        
        self.total = 1
        visited.add(0)
        for s in e[0]:
            dfs(s)
        
        return self.total