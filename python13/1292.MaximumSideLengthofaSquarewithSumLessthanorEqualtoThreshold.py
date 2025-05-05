class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        prefix = [[0]*(n+1) for _ in range(m+1)]
        
        for i, j in product(range(m), range(n)):
            prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + mat[i][j]

        length = 0
        for i in range(m):
            for j in range(n):
                while i+length <= m and j + length <= n and prefix[i+length][j+length] - prefix[i][j+length] - prefix[i+length][j] + prefix[i][j] <= threshold:
                    length += 1

        return length - 1
    
