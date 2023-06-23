class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        """
        
        O(m*n ^2)
        
        O(m^2*n)
        
        """
        m = len(matrix)
        n = len(matrix[0])
        
        maxrect = [[0 for i in range(n)] for j in range(m)]
        
        
        for i in range(m):
            for j in range(n):
                maxrect[i][j] = int(matrix[i][j])
                if i > 0 and maxrect[i-1][j] >0 and maxrect[i][j] >0:
                    maxrect[i][j] += maxrect[i-1][j]

        maxA = 0
        #print()
        
        for i in range(m):
            #print("HERE")
            s = []
            h = 0
            for j in range(n):
                #print("THERE")
                h = maxrect[i][j]
                #print(h)
                start = j
                while s and s[-1][1] > h:
                    index,height = s.pop()
                    maxA = max(maxA, height * (j - index))
                    start = index
                s.append((start,h))
            for val in s:
                maxA = max(maxA, val[1] * (n - val[0] ))
        
        return maxA