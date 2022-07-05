class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        """
        
        Dijkstra
        
        """
        
        
        h = []
        
        edges = defaultdict(list)
        for t in times:
            edges[t[0]].append((t[1],t[2]))
        
        heapq.heappush(h,[0,k])
        
        visited = set()
        
        t = 0
        
        while h:
            time, cur = heapq.heappop(h)

            visited.add(cur)

            if len(visited) == n:
                return time

            for edge in edges[cur]:
     
                if edge[0] not in visited:
                    heapq.heappush(h,[time + edge[1], edge[0]])

        return -1

        