class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:

        
        '''
        M = len(grid)
        N = len(grid[0])
        
        rows = defaultdict(list)

        cols = defaultdict(list)

        #for i in range(M):
        #    rows[i] = sorted()

        hm = defaultdict()
        
        #@cache
        def dfs(i,j):
            
            if (i,j) in hm:
                return hm[(i,j)]
            
            p = 0
            
            k = 1
            nk = -1
            nv = float('inf')
            
            nks = set()
            
            while i + k < M:
                if grid[i+k][j] > grid[i][j] and grid[i+k][j] <= nv:
                    nks = set()
                    nks.add(i+k)
                    nv = grid[i+k][j]
                    nk = i+k
                elif grid[i+k][j] > grid[i][j] and grid[i+k][j] == nv:
                    nv = grid[i+k][j]
                    nk = i+k
                    nks.add(i+k)
                    #p = max(p, dfs(i+k,j)+1)
                k+=1
            
            #if nk != -1:
            #    p = max(p, dfs(nk,j)+1)
            
            k = 1
            #nk = -1
            #nv = float('inf')
            
            while i - k >=0:
                if grid[i-k][j] > grid[i][j] and grid[i-k][j] <= nv:
                    nv = grid[i-k][j]
                    nk = i-k
                    nks = set()
                    nks.add(i-k)
                elif grid[i-k][j] > grid[i][j] and grid[i-k][j] == nv:
                    nv = grid[i-k][j]
                    nk = i-k
                    nks.add(i-k)
                
                k+=1

            if nk != -1:
                #for s in nks:
                p = max(p, dfs(nk,j)+1)
            
            nk = -1
            nv = float('inf')
            nks = set()
            
            k = 1
            while j + k < N:
                if grid[i][j+k] > grid[i][j] and grid[i][j+k] <= nv:
                    nv = grid[i][j+k]
                    nk = j+k
                    nks = set()
                    nks.add(j+k)
                elif grid[i][j+k] > grid[i][j] and grid[i][j+k] == nv:
                    nks.add(j+k)
                    
                k+=1
            #if nk != -1:
            #    p = max(p, dfs(i,nk)+1)
            
            #nk = -1
            #nv = float('inf')
            
            k = 1
            while j - k >=0:
                if grid[i][j-k] > grid[i][j] and grid[i][j-k] <= nv:
                    nv = grid[i][j-k]
                    nk = j-k
                    nks = set()
                    nks.add(j-k)
                elif grid[i][j-k] > grid[i][j] and grid[i][j-k] == nv:
                    nks.add(j-k)

                k+=1
                
            if nk != -1:
                #for s in nks:
                #    p = max(p, dfs(i,s)+1)
                p = max(p, dfs(i,nk)+1)
            
            hm[(i,j)] = p
            return p

        m = 0
        
        v= set()
        
        for i in range(M):
            for j in range(N):
                m = max(m, dfs(i,j))
        
        return m +1
        


        
        
        M = len(grid)
        N = len(grid[0])
        
        rows = defaultdict(list)

        cols = defaultdict(list)
        
        
        #for i in range(M):
        #    rows[i] = sorted()
        
        
        @cache
        def dfs(i,j):
            
            p = 0
            
            k = 1
            nk = -1
            nv = float('-inf')
            
            while i + k < M:
                if grid[i+k][j] > grid[i][j] and grid[i+k][j] > nv:
                    nv = grid[i+k][j]
                    nk = i+k
                    #p = max(p, dfs(i+k,j)+1)
                k+=1
            
            p = max(p, dfs(nk,j)+1)
            
            k = 1
            nk = -1
            nv = float('-inf')
            
            while i - k >=0:
                if grid[i-k][j] > grid[i][j]:
                    p = max(p, dfs(i-k,j)+1)
                k+=1
            p = max(p, dfs(nk,j)+1)
            
            nk = -1
            nv = float('-inf')
            
            k = 1
            while j + k < N:
                if grid[i][j+k] > grid[i][j]:
                    p = max(p, dfs(i,j+k)+1)
                k+=1
            
            p = max(p, dfs(i,nk)+1)
            
            nk = -1
            nv = float('-inf')
            
            k = 1
            while j - k >=0:
                if grid[i][j-k] > grid[i][j]:
                    p = max(p, dfs(i,j-k)+1)
                k+=1
            
            p = max(p, dfs(i,nk)+1)
            
            return p

        m = 0
        
        v= set()
        
        for i in range(M):
            for j in range(N):
                m = max(m, dfs(i,j))
        
        return m +1
        
        
        '''
                
        dic = defaultdict(list)
        m = len(mat)
        n = len(mat[0])
        
        for row in range(m):
            for col in range(n):
                dic[mat[row][col]].append((row, col))

        rows = [0] * m
        cols = [0] * n

        for _, arr in sorted(dic.items()):
            curr = []
            for r, c in arr:
                curr.append(1 + max(rows[r], cols[c]))
            
            for i in range(len(arr)):
                r, c = arr[i]
                x = curr[i]
                rows[r] = max(rows[r], x)
                cols[c] = max(cols[c], x)

        return max(rows + cols)
