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