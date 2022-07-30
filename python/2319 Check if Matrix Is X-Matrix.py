class Solution:
    def checkXMatrix(self, g: List[List[int]]) -> bool:
        n = len(g)
        
        
        for i in range(n):
            for j in range(n):

                if i == j and g[i][j] == 0:
                    return False
                
                if i + j == n-1 and g[i][j] == 0:
                    return False
                
                if i != j and i + j != n-1 and g[i][j] != 0:
                    return False

        return True
