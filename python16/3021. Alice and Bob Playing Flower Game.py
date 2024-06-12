class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        
        
        '''
        
        A x  B y A
        
        A  B  A
        
        
        '''
        #def dp(x,y, turn):
        #    if x == 0 and y == 0:
        #        if turn :
        '''
        def dp(x, turn):
            if x == 0:
                if turn :
                    return 1
                else:
                    return 0
            
            return dp(x-1, not turn)
        
        
        return dp(n+m, True)
        '''
        
        pa = 0
        ima = 0
        
        for i in range(1,m+1):
            if i % 2 == 0:
                pa += 1
            else:
                ima += 1
        
        #print(pa,ima)
        res = 0
        for i in range(1,n+1):
            
            #for j in range(1,m+1):
            #    if abs(i-j) % 2 == 1:
            #        res += 1
            res +=  ima if i % 2 == 0 else pa
            #res +=  (m - 2) // 2 if i % 2 == 0 else (m - 1) // 2
            
            #res += (m - 1) // 2
            '''
            Y = i + 1
            while Y >= 0:
                if Y >= 1 and Y <= m:
                    res += 1
                Y -= 2
            '''
            '''
            Y = i + 1
            
            if Y >= 1 and Y <= m:
                res += 1
            
            Y = i - 1

            if Y >= 1 and Y <= m:
                res += 1
            '''
        return res