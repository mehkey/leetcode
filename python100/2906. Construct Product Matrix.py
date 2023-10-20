class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        M = len(grid)
        N = len(grid[0])
        
        res = [ [0]*N for i in range(M) ]
        
        pre = [1] * (M*N)
        suf = [1] * (M*N)
        
        for i in range(M):
            for j in range(N):
                pre[i*N+j] *= grid[i][j] 
                if i*N+j-1 >= 0:
                    pre[i*N+j] *= pre[i*N+j-1]
                pre[i*N+j] %= 12345

        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                suf[i*N+j] *= grid[i][j]
                if i*N+j+1 < M*N:
                    suf[i*N+j] *= suf[i*N+j+1]
                suf[i*N+j] %= 12345

        rr = [0] * (M*N)
        
        for i in range(M):
            for j in range(N):
                res[i][j] = (pre[i*N+j-1] if i*N+j-1 >= 0 else 1) * (suf[i*N+j+1] if i*N+j+1 < M*N else 1)
                res[i][j] %= 12345
        return res
            
        
        '''
        tz = 0
        tzl = (0,0)
        tot = 1
        
        for i in range(M):
            for j in range(N):
                res[i][j] = tot
                
                
                if grid[i][j] % 12345 == 0:
                    tz += 1

                #tot *= grid[i][j]
                #tot %= 12345
        ttt = tot
        
        for i in range(M):
            for j in range(N):
                res[i][j] = (tot // grid[i][j]) % 12345
                #res[i][j] %= 12345
        
        if tz == 1:
            
            tot = 1
            for i in range(M):
                for j in range(N):
                    if grid[i][j] % 12345 != 0:
                        tot *= grid[i][j]
                        tot %= 12345
                    else:
                        tzl = (i,j)

            res[tzl[0]][tzl[1]] = tot

        #if tz >= 2:
            #res = [ [0]*N for i in range(M)]
            #return res

        return res
        '''