class Solution:
    def deleteString(self, s: str) -> int:

        '''
        n = 0
        
        
        @cache
        def dp1(i):
            
            m = 1
            
            l = len(s) - i
            
            if len(set(s[i:])) == 1:
                m = len(set(s[i:]))
            
            for j in range(i+1, i + 1 + (l)//2 ):
                
                left = s[i:j] #getS(i,j)
                #print("left" , left)
                if j + len(left) > len(s):
                    continue
                
                right = s[j:j + len(left)] # getS(j,j + len(left)) # s[j:j + len(left)]
                #print("right" ,right)
                
                if left == right:
                    
                    m = max(m,1+ dp1(j))
                    #return 1+ dp1(j)
                    #return 1+ dp(j)
            
            return m
        
        return dp1(0)

        
        @cache
        def dp(i):
            
            #if i <= 0:
            #    return 0

            m = 1
            
            l = i 
            
            #print("i+1", i+1)
            #print("other", i + 1 + (l)//2 )
            
            
            for j in range(i-1, i - 1 - (l)//2 , -1):
                
                left = s[j:i]
                #print("left" , left)
                if j + len(left) > len(s):
                    continue
                
                right = s[j -len(left) :j ] # s[j:j + len(left)]
                #print("right" ,right)
                
                if left == right:
                    
                    #return 1 + dp(j)
                    m = max(m, 1+ dp(j))
                    #return 1+ dp(j)
            
            return m

        return dp(len(s)) #max(dp(len(s)), dp1(0))
        
        
        
        
        
        @cache
        def dp2(i,k):
            
            m = 1
            
            l = k - i
            
            w = 1
            
            for j in range(i+1, i + 1 + (l)//2 ):

                val = 1
                
                #left = s[i:j]
                
                left = s[i:j] 
                print(left)
                
                if j + len(left) > len(s):
                    continue
                
                right = s[j:j + len(left)] 
                
                if left == right:

                    val =  1+ dp2(j,k)
                
                left = s[k-w:k]
                print("left" , left)
                #if j + len(left) > len(s):
                #    continue
                
                right = s[k-w-len(left) :k-w ] # s[j:j + len(left)]
                print("right" ,right)
                
                if left == right:
                    
                    #return 1 + dp(j)
                    val = max(val, 1+ dp2(i,k-w))
                    #return 1+ dp(j)
                
                if val != 1:
                    return val

                w += 1
                
            return m
        
        return dp2(0,len(s))
        
        
        
        '''
        n = len(s)
        if len(set(s)) == 1:
            return n
        dp = [1] * n
        for i in range(n - 2, -1, -1):
            for l in range(1, (n - i) // 2 + 1):
                if s[i : i + l] == s[i + l : i + 2 * l]:
                    dp[i] = max(dp[i], 1 + dp[i + l])
        return dp[0]
        