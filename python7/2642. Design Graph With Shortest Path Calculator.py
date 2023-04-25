class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.G = defaultdict(list)
        
        for e in edges:
            heappush(self.G[e[0]], (e[2],e[1]))
        

    def addEdge(self, edge: List[int]) -> None:
        heappush(self.G[edge[0]], (edge[2],edge[1]))

    def shortestPath(self, node1: int, node2: int) -> int:
        
        if node1 == node2:
            return 0
        
        if node1 not in self.G:
            return -1
        
        h = self.G[node1][::]

        p = 0
        
        v = set()
        
        v.add(node1)
        
        
        while h:
            dis,cur = heappop(h)
            
            v.add(cur)
            if cur == node2:

                return dis
            
            for nex in self.G[cur]:
                if nex[1] not in v:
                    #print(nex)
                    #v.add(nex[1])
                    heappush(h, (dis+nex[0], nex[1]))

        return -1

import heapq

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adj_list = {i: [] for i in range(n)}
        for edge in edges:
            self.adj_list[edge[0]].append((edge[1], edge[2]))
        
    def addEdge(self, edge: List[int]) -> None:
        self.adj_list[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        dist = {i: float('inf') for i in range(len(self.adj_list))}
        dist[node1] = 0
        
        while heap:
            (d, node) = heapq.heappop(heap)
            if node == node2:
                return d
            if d > dist[node]:
                continue
            for neighbor, weight in self.adj_list[node]:
                new_dist = d + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))
                    
        return -1
# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)