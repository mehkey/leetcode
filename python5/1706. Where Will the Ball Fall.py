class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        '''
        temp = [i for i in range(len(grid[0]))]
        #print(temp)
        for i in range(len(grid)):

            g = grid[i]
            for j in range(len(g)):

                if temp[j] != -1:

                    if temp[j] == 0 and g[j] == -1:
                        temp[j] = -1
                    elif temp[j] == len(g) -1 and g[j] == 1:
                        temp[j] = -1
                    elif temp[j] < len(g) -1 and g[temp[j]] == 1 and g[temp[j]+1] == -1:
                        temp[j] = -1
                    elif temp[j] > 0 and g[temp[j]] == -1 and g[temp[j]-1] == 1:
                        temp[j] = -1
                    else:
                        temp[j] += g[j]
            #print(temp)
        return temp
        '''
        r_len = len(grid)
        c_len = len(grid[0])
        output = list(range(c_len))
        
        for r in range(r_len):
            for i in range(c_len):
                c = output[i]
                if c == -1: continue
                c_nxt = c + grid[r][c]
                if c_nxt < 0 or c_nxt >= c_len or grid[r][c_nxt] == -grid[r][c]:
                    output[i] = -1
                    continue
                output[i] += grid[r][c]
        
        return output