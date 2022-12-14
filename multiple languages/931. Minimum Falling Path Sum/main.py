class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        res = 0
        cur= [matrix[0][i] for i in range(len(matrix[0]))]

        for i in range(1,len(matrix)):
            new_cur = [0] * len(matrix[0])
            for j in range(len(matrix[0])):
                new_cur[j] = matrix[i][j] + min(cur[j-1] if j>0 else float('inf'),cur[j],cur[j+1] if j+1<len(matrix[0])else float('inf'))

            cur = new_cur
        return min(cur)

