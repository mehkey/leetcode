class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        mmm = matrix[::-1]
        n = len(matrix)
        m = len(matrix[0])
        res =[]
        for i in range(n):
            for j in range(m):
                
                row = matrix[i]
                
                col = [matrix[x][j] for x in range(n)]

                if matrix[i][j] == min(row) and matrix[i][j] == max(col):
                    res.append(matrix[i][j])
        
        return res
                    