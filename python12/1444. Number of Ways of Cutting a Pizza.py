class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        
        M = len(pizza)
        N = len(pizza[0])
        
        MOD = 10**9+7

        @cache
        def has_apple(start_row, start_col, end_row, end_col):
            for r in range(start_row, end_row+1):
                for c in range(start_col, end_col+1):
                    if pizza[r][c] == 'A':
                        return True 
            return False 

        @cache
        def dp(si,sj, k):
            if k == 0:
                return has_apple(si,sj,M-1,N-1)
            
            num_ways = 0 
            
            for i in range(si+1,  M):
                if has_apple(si, sj, i-1, N-1):
                    num_ways += dp(i, sj, k-1)

            for j in range(sj+1,  N):
                if has_apple(si, sj, M-1, j-1):
                    num_ways += dp(si, j, k-1)

            return num_ways 
        
        return dp(0,0, k-1) % MOD
        '''
            if k == 0:
                return 1
            
            if si >= ei or sj >= ej:
                return 1
            
            xx = set()
            yy = set()

            for i in range(si,ei+1):
                
                for j in range(sj, ej+1):
                    
                    if pizza[i][j] == 'A':
                        xx.add(i)
                        yy.add(j)
            
            resX = 1
            #resY = 1

            if len(xx) > 1:
                xx =  sorted(xx) 
                #print(xx)
                count = 0
                
                xWays = 0
                for i in range(si,ei+1):
                    if i in xx:
                        count += 1
                    
                    if count >= 1 and count != len(xx):

                        resX *= (dp(si, sj, xx[i],ej, k-1)% MOD
                        resX *= dp(xx[i]+1, sj, ei,ej, k-1))  % MOD
            if len(yy) > 1:
                yy =  sorted(yy) 
                #print(yy)
                #for j in range(len(yy)):
                count = 0
                for j in range(sj, ej+1):
                    if j in yy:
                        count += 1
                    if count >= 1 and count != len(yy) :

                        resX *= dp(si, sj , ei,yy[j], k-1) % MOD
                        resX *= dp(si, yy[j] , ei,ej, k-1) % MOD
            
            return (resX) % MOD
                
                
        return dp(0,0, N-1, M-1, k-1) % MOD
        '''