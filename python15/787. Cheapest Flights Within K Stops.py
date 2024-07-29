class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        
        def bellman_ford(n,k, edges, start):
            dist = [float("inf")] * n
            pred = [None] * n

            dist[start] = 0

            for _ in range(k+1):
                temp = dist[:]
                for u, v, d in edges:
                    if dist[u] + d < temp[v]:
                        temp[v] = dist[u] + d
                        pred[v] = u
                dist = temp

            return dist, pred
        
        
        dest, pred  = bellman_ford(n,k, flights, src)
        # print(dest)

        return -1 if dest[dst] == inf else dest[dst]
        
        