class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        l = 0
        r = len(matrix) -1
        
        while ( l < r):
            up = l
            down = r
            for i in range(0, r-l):
                
                tmp = matrix[l+i][up]
                matrix[l+i][up] = matrix[r][up+i]
                matrix[r][up+i] = matrix[r-i][down]
                matrix[r-i][down] = matrix[l][down-i]
                matrix[l][down-i] = tmp
                
            l +=1
            r -=1
        
        return
            
        