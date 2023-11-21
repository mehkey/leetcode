class Solution:
    def minIncrementOperations(self, nn: List[int], k: int) -> int:
        n = len(nn)
        
        @cache
        def dp(i, lag):
            
            
            if i == n:
                return 0
            
            if lag == 2:
                return max(k-nn[i],0) + dp(i+1,0)
            
            if lag == 1:
                return min( max(k-nn[i],0) + dp(i+1,0), dp(i+1,lag + 1)  )
            
            return min( max(k-nn[i],0) + dp(i+1,0), dp(i+1,lag + 1), dp(i+1,lag + 2)  )

            '''
            #if i == n -1:
                #return max(k-nn[n-1],0)

            #if i == n -2:
                #return min( max(k-nn[n-1],0) , max(k-nn[n-2],0)  )

            m0,m1,m2 = nn[i], nn[i+1], nn[i+2]
            
            m = max(k-m0,0) + dp(i+1)
            
            m = min( m, max(k-m1,0) + dp(i+2))
            
            m = min( m, max(k-m2,0) + dp(i+3))
            
            return m
            '''

        return dp(0,0) 
        '''
        n = len(nn)
        
        tot = 0
        #print(nn,k)
        
        
        for i in range(n):
            
            if i + 2 >= n:
                break
            
            m0,m1,m2 = nn[i], nn[i+1], nn[i+2]
            #m = max(m0,m1,m2)
            
            m3 = nn[i+3] if i +3 < n else k
            m4 = nn[i+4] if i + 4 < n else k
            m5 = nn[i+5] if i +5 < n else k
            
            #s0 = max(0,k-m0) + max( max( k-m3, k-m4,k-m1) ,0)
            #s1 = max(0,k-m1) + max( k - m4 ,0)
            #s2 = max(0,k-m2) #+ max( k - max(m3,m4,m5) ,0)
            
            s0 = max(0,k-m0) +  max( min(  k-m3, (k-m2) if i + 4 < n else 0, (k-m1) if i + 3 < n else 0) ,0)  
            s1 = max(0,k-m1) +  max( min( (k-m2) if i + 3 < n else 0, k-m3, k-m4) ,0)
            s2 = max(0,k-m2)  + max( min(  k-m3, k-m4,k-m5) ,0)#+  max( max(m3,m4,m5) ,0)
            #print(s0,s1,s2)
            sm = min(s0,s1,s2)
            idd = -1
            
            m = max(m0,m1,m2)
            
            if m >=k:
                continue
            
            #print(s0,s1,s2)

            if s2 == sm:
                idd = i+2
                nn[idd] += k - m2
                tot += k - m2
            elif s1 == sm:
                idd = i+1
                nn[idd] += k - m1
                tot += k - m1
            elif s0 == sm:
                idd = i
                nn[idd] += k - m0
                tot += k - m0  
            
            #print(m,idd)
            #if m < k:
                #nn[idd] += k - m
                #tot += k - m
        
        return tot
                
        '''