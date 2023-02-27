684. Redundant Connection
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        """
        node      1 2 3
        parent = [1,2,3]
        rank =   [1,1,1]
        
        find
        
        (for each edge) find parent if same parent -> return edge
        
        union
        
        (for each edge) update the rank, udpdate the parent of each node
        
        """
        
        m=0
        for edge in edges:
            m = max(m,edge[0],edge[1])
        
        parent = [i for i in range(0,m+1)]

        rank = [1] * (m +1)
        
        #print(parent)
        #print(rank)
        
        def find(n):
            p = parent[n]
            
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            
            return p
        
        for edge in edges:
            
            if find(edge[0]) == find(edge[1]):
                return edge
            
            orderededge = edge
            
            if rank[edge[0]] > rank[edge[1]]:
                orderededge = [edge[1],edge[0]]
            
            rank[orderededge[0]] += rank[orderededge[1]]
            
            parent[edge[1]] = edge[0]
        
        return
            