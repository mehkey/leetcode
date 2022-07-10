class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        ROWS, COLS = len(matrix) , len(matrix[0])

        d = [[0,1],[0,-1],[1,0],[-1,0]]

        LIP = [[0]* COLS] * ROWS

        #print(LIP)

        def dfs(r,c, prev):

            if r < 0 or r >= ROWS or c < 0 or c >= COLS or matrix[r][c] <= prev:
                return 0

            if LIP[r][c] != 0 :
                return LIP[r][c]

            prev= matrix[r][c]
            res = 1
            res = max(res,1+dfs(r+d[0][0],d[0][1],prev))
            res = max(res,1+dfs(r+d[1][0],d[1][1],prev))
            res = max(res,1+dfs(r+d[2][0],d[2][1],prev))
            res = max(res,1+dfs(r+d[3][0],d[3][1],prev))

            LIP[r][c] = res
            print(r, ' ' , c, ' res ', res)

            return res

        maxRes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if LIP[r][c] == 0:
                    print("HERE")
                    maxRes = max(dfs(r,c,-1),maxRes)
        
        return maxRes





        class Solution:
    #def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    """
    ROWS, COLS = len(matrix) , len(matrix[0])

    d = [[0,1],[0,-1],[1,0],[-1,0]]

    LIP = [[0]* COLS] * ROWS

    #print(LIP)

    def dfs(r,c, prev):

        if r < 0 or r >= ROWS or c < 0 or c >= COLS or matrix[r][c] <= prev:
            return 0

        if LIP[r][c] != 0 :
            return LIP[r][c]

        prev= matrix[r][c]
        res = 1
        res = max(res,1+dfs(r+d[0][0],d[0][1],prev))
        res = max(res,1+dfs(r+d[1][0],d[1][1],prev))
        res = max(res,1+dfs(r+d[2][0],d[2][1],prev))
        res = max(res,1+dfs(r+d[3][0],d[3][1],prev))

        LIP[r][c] = res
        print(r, ' ' , c, ' res ', res)

        return res

    maxRes = 0

    for r in range(ROWS):
        for c in range(COLS):
            if LIP[r][c] == 0:
                print("HERE")
                maxRes = max(dfs(r,c,-1),maxRes)

    return maxRes

    
        
    def longestIncreasingPath(self, matrix):
        def length(z):
            
            if z not in memo:
                
                memo[z] = 1 + max([length(Z)
                                   for Z in [z+1, z-1, z+1j, z-1j]
                                   if Z in matrix and matrix[z] > matrix[Z]]
                                  or [0])
            return memo[z]

        memo = {}
        matrix = {i + j*1j: val
                  for i, row in enumerate(matrix)
                  for j, val in enumerate(row)}

        print(matrix)
        print(memo)

        m =  max(map(length, matrix), default = 0)
        print(memo)
        return m
    """

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        if rows == 0:
            return 0
        
        cols = len(matrix[0])
        indegree = [[0 for x in range(cols)] for y in range(rows)] 
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        
        for x in range(rows):
            for y in range(cols):
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if nx >= 0 and ny >= 0 and nx < rows and ny < cols:
                        if matrix[nx][ny] < matrix[x][y]:
                            indegree[x][y] += 1
                            
        queue = []
        for x in range(rows):
            for y in range(cols):
                if indegree[x][y] == 0:
                    queue.append((x, y))
    
        path_len = 0
        while queue:
            sz = len(queue)
            for i in range(sz):
                x, y = queue.pop(0)
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if nx >= 0 and ny >= 0 and nx < rows and ny < cols:
                        if matrix[nx][ny] > matrix[x][y]:
                            indegree[nx][ny] -= 1
                            if indegree[nx][ny] == 0:
                                queue.append((nx, ny))
            path_len += 1
        return path_len 
