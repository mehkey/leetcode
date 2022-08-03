class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        """
        
        
        1 0 1
        1 0 1
        1 0 1
        
        
        0.0 0
        0 0 0
        0 0 0
        
        
        1 0
        0 0
        
        2 1
        1 1
        
        
        1 0 1 1
        0 1 1 1
        1 1 1 1
        1 1 1 1
    
        0.0 0 1
        0 3 2 1
        0 2 2 1
        1 1 1 1
        
        min( right
        down
        down right) + 1
        
        
        
        cache = {}
        
        m = 0
        
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                #print(i, " ", j)
                
                if i == len(matrix)-1 or j == len(matrix[0]) - 1:
                    #print('here')
                    #print(matrix[i][j])
                    
                    if matrix[i][j] == '1':
                        cache[(i,j)]  = 1
                    else:
                        cache[(i,j)]  = 0
                else:
                    #print('there')
                    if matrix[i][j] == "1" :
                        cache[(i,j)] = min(cache[(i+1,j)], cache[(i,j+1)], cache[(i+1,j+1)]) + 1                    
                    else:
                        cache[(i,j)] = 0
                
                m = max(m, cache[(i,j)]*cache[(i,j)])
                #print(cache)
                #print(m)

        return m
    
         """
        cache = [[ 0 for i in range(len(matrix[0])) ] for y in range(len(matrix))]
        #cache[4][4] = 1
        #print(matrix)
        #print(cache)
        
        m = 0
        
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                #print(i, " ", j)
                
                if i == (len(matrix)-1) or j == (len(matrix[0]) - 1):
                    #print("inside")

                    if matrix[i][j] == "1":
                        #print(i, " ", j)
                        #print(cache)
                        cache[i][j] = 1
                        #print("HERE")
                        #print(cache)
                    else:
                        cache[i][j] = 0
                else:
                    #print('there')
                    if matrix[i][j] == "1" :
                        cache[i][j] = min(cache[i+1][j] , cache[i][j+1] , cache[i+1][j+1] ) + 1
                    else:
                        cache[i][j] = 0

                m = max(m, cache[i][j] *cache[i][j] )
                #print(cache)
                #print(m)

        #print(cache)
        #print(m)
        return m
                        
        