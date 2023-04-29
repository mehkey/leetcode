class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        
        M = len(grid)
        N = len(grid[0])
        
        x,y = 0,0
        
        dirs = ((1,2),(2,1),(2,-1),(-2,1),(-2,-1),(1,-2),(-1,-2),(-1,2))
        
        cur_val = 0
        
        v = set()
        
        while True:
            
            if cur_val >= M * N :
                return False
            
            #print(x,y)
            #print(cur_val)
            v.add((x,y))
            
            found = False

            for d in dirs:
                
                nx = x+d[0]
                ny = y+d[1]
                
                if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == cur_val+1 and (nx,ny) not in v:
                    cur_val += 1
                    x = nx
                    y = ny
                    found  = True
                    
                    if cur_val == (M * N) -1:
                        return True
                    
                    break

            if not found:
                return False
        
        return True
            
            
                    
            
            
            
        
        