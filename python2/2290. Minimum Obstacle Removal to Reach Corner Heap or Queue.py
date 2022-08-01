class Solution:

    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
        
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        
        distances = [[-1] * C for _ in range(R)]
        
        q = deque([(0, 0, 0)])
        
        while q:
            for _ in range(len(q)):
                dist, r, c = q.popleft()
                
                for dr, dc in d:
                    rr, cc = r + dr, c + dc
					#Check if the cell is inbounds and has not been visited before
                    if 0 <= rr < R and 0 <= cc < C and distances[rr][cc] == -1:
                        
                        #If the cell is an obstacle - assign current distance + 1 to its value
                        if grid[rr][cc] == 1:
                            distances[rr][cc] = dist + 1
                            q.append((dist + 1, rr, cc))

                        else:
                            #Make sure we process cells with less obstacles first hence appendleft
                            distances[rr][cc] = dist
                            q.appendleft((dist, rr, cc))
                            
        return distances[R - 1][C - 1]



class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        visited = [[False]*m for _ in range(n)]
        
        paths = [ (0,-1),(-1,0),(0,1),(1,0)]
        
        queue = [(0,0,0)]  #val, x,y will be pushed

        while queue:
            val,i,j = heappop(queue)
            if i == n-1 and j==m-1:
                return val + grid[i][j]

            for x,y in paths:
                x1 = i+x
                y1 = j+y
                
                if (x1>=0 and x1<n and y1>=0 and y1<m and not visited[x1][y1]):
                    visited[x1][y1] = True
                    heappush(queue, (val + grid[x1][y1], x1, y1))
                    
        return -1