class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        
        ans = ConnectedComponents().connectedComponents(n, edges)

        return ans

class ConnectedComponents:
    def merge(self, parent, x):
        if parent[x] == x:
            return x
        return self.merge(parent, parent[x])
 
    def connectedComponents(self, n, edges):
        parent = [i for i in range(n)]

        for x in edges:
            parent[self.merge(parent, x[0])] = self.merge(parent, x[1])

        graph = defaultdict(set)
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
        
        for i in range(n):
            parent[i] = self.merge(parent, parent[i])

        m = collections.defaultdict(list)
        for i in range(n):
            m[parent[i]].append(i)
        
        
        sans = set()
        for i in range(n):
            if parent[i] == i:
                sans.add(i)

        ans = 0

        for i in range(n):
            
            if len(m[parent[i]]) != len(graph[i])+1:
                if parent[i] in sans:
                    sans.remove(parent[i])
            
        return len(sans)