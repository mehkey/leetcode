import numpy
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp=[[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]==0:
                    continue
                if row==0:
                    dp[row][col]=1
                elif col==0:
                    dp[row][col]=1
                else:
                    minimum=min(dp[row-1][col],dp[row][col-1],dp[row-1][col-1])
                    dp[row][col]=minimum+1
        return sum(numpy.concatenate(dp))