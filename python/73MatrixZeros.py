class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)

        n = len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    
                    if i == 0:
                        first_row_has_zero = True
                    if j == 0:
                        first_col_has_zero = True
                    
                    matrix[i][0] = matrix[0][j] = 0

        #print(matrix)
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        #print(matrix)
        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        #print(matrix)
        #print(first_row_has_zero)
        #print(first_col_has_zero)
    
        if first_row_has_zero:
            #print("HERE")
            for j in range(n):
                #print("HERE", j)

                matrix[0][j] = 0
                #print(matrix[0][j])
        
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
        #print(matrix)