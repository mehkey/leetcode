class NumMatrix:


    def __init__(self, matrix: List[List[int]]):
        self.m = matrix.copy()
        
        #[[0] * len(matrix[0])] * len(matrix)
        
        for i in range(0, len(matrix)):
            for j in range(0 , len(matrix)):
                if i > 0 and j > 0:
                    self.m[i][j] +=  self.m[i-1][j] + self.m[i][j-1] - self.m[i-1][j-1]
                elif i> 0:
                    self.m[i][j] +=  self.m[i-1][j] 
                elif j>0:
                    self.m[i][j] +=  self.m[i][j-1] 
        
        #print(self.m)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        return self.m[row2][col2] - self.m[row1-1][col2] - self.m[row2][col1-1] + self.m[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)