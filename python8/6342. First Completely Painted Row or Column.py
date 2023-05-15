class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        M = len(mat)
        N = len(mat[0])
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        
        rowsC = defaultdict(int)
        colsC = defaultdict(int)
        
        nums = defaultdict(tuple)
        for i in range(M):
            rowsC[i] = N
            for j in range(N):
                rows[mat[i][j]].add(i)
                cols[mat[i][j]].add(j)
                nums[mat[i][j]] = (i,j)
                colsC[j] = M

        for i,a in enumerate(arr):

            rowsC[nums[a][0]] -= 1
            
            if rowsC[nums[a][0]] == 0:
                return i

            colsC[nums[a][1]] -= 1

            if colsC[nums[a][1]] == 0:
                return i

        return -1
    

    m = len(mat)
    n = len(mat[0])
    map = {}
    for i in range(m):
        for j in range(n):
            map[mat[i][j]] = [i, j]
    row = [0] * m
    col = [0] * n
    for i in range(len(arr)):
        x = map[arr[i]]
        row[x[0]] += 1
        col[x[1]] += 1
        if row[x[0]] == n or col[x[1]] == m:
            return i
    return -1