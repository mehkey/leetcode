class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:


        h = grid[0]
        
        for i in range(0,len(grid)-1):
            tmp = [float("inf")] * len(grid[0])
            
            for j in range(len(grid[0])):
                #print(j)
                #print(moveCost[grid[i][j]])
                for ii, c in enumerate(moveCost[grid[i][j]]):
                    tmp[ii] = min(tmp[ii], h[j] + c + grid[i+1][ii])
            #print(tmp)
            h = tmp

        return min(h)

        """
        for g in grid[0]:
            for m in moveCost[0]:
                heapq.heappush(h, (g,,d) )

        index = 1
        
        
        while h :
            
            for _ in range(len(h)):
                
                c,n,c = heapq.heappop(h)
                
                for m in moveCost[index]:
                    heapq.heappop(h, () )

        return -1
        
        """
            
            