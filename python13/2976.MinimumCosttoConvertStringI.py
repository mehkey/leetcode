def dijkstra(graph, start):
    """ 
        Uses Dijkstra's algortihm to find the shortest path from node start
        to all other nodes in a directed weighted graph.
    """
    n = len(graph)
    dist = defaultdict(lambda: float("inf"))
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len == dist[v]:
            for w, edge_len in graph[v]:
                if edge_len + path_len < dist[w]:
                    dist[w] = edge_len + path_len
                    heappush(queue, (edge_len + path_len, w))

    return dist

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        N = len(original)
        M = len(source)
        G = defaultdict(list)
        for i in range(N):
            G[original[i]].append((changed[i],cost[i]))
        
        DG = {}
        for i in range(0,27):
            let = chr(i + ord('a'))

            dist = dijkstra(G,let)
            DG[let] = dist

        res = 0
        for i in range(M):
            o,d = source[i],target[i]

            if DG[o][d] == float('inf'):
                return -1
            res += DG[o][d]

        return res