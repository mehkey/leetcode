class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        M = len(grid)
        N = len(grid[0])

        diff = [[0 for j in range(N)] for i in range(M)]

        oR = [0 for i in range(M)]

        oC = [0 for i in range(N)]

        zR = [0 for i in range(M)]

        zC = [0 for i in range(N)]

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    zR[i] += 1
                    zC[j] += 1
                elif grid[i][j] == 1:
                    oR[i] += 1
                    oC[j] += 1

        for i in range(M):
            for j in range(N):
                diff[i][j] = oR[i] + oC[j] - zR[i] - zC[j]
        
        return diff