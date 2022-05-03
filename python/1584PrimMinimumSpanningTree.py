class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        #prims algorithm
        
        #connecting all tree

        N = len(points)

        h = []

        visited = set()

        link = {i:[] for i in range(N) }

        for i in range(N):
            for j in range( i+1, N):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1] )
                link[i].append([distance,j])
                link[j].append([distance,i])

        total = 0

        #visited.add(0)
        
        heapq.heappush(h,[0,0])
    
    
        #print(link)
        while len(visited) < N:
            
            #print (h)

            
            cost, node = heapq.heappop(h)
            #print (cost, " " , node)

            
            if node in visited:
                continue
            
            total += cost
            visited.add(node)

            for l in link[node]:
                
                heapq.heappush(h,l)
            
            
        return total