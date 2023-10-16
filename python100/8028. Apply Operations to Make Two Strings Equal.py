class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:

        n = len(s1)
        r = [0] * n
        t = 0

        for i in range(n):
            if s1[i] != s2[i]:
                r[i] = 1
                t += 1

        if t %2 != 0:
            return -1

        @cache
        def dp(i,cur):

            if cur is None:
                cur = r[i] 

            if i == n-1:
                return cur * (x / 2 )

            if cur == 0:
                return dp(i+1, None)

            return min( x / 2 + dp(i+1, None ), 1+ dp(i+1, 1-r[i+1]))

        return int(dp(0,None))

    

    

        s2 = [int(i) for i in s2]
        s1 = [int(i) for i in s1]

        def bitt(bitlist):
            out = 0
            for bit in bitlist:
                out = (out << 1) | bit
            return out

        def flip(arr,i):
            '''
            if arr[i] ==0:
                arr[i] =1
            else:
                arr[i] = 0
            
            if arr & 1 << i:
                arr |= 1 << i
            else:
                arr &= 0 << i
            '''  
            
            return arr ^ (1 << i)
        
            if arr & 1 << i:
                arr |= 1 << i
            else:
                arr ^= (1 << i)
            #arr = arr ^ (1 << i)
            
            return arr

        #@cache
        def dp(i, arr):
            if i == len(s1):
                #print(arr, s2)
                if s2 == arr:
                    #print('EQUAL')
                    return 0
                else:
                    return float('inf')
            
            if s2[i] == arr[i]:#arr >> i & 1:
                return dp(i+1, arr)
            else:
                
                #print(i, "not equal", s2, arr)
                m = float('inf')

                if i + 1 < len(s1):
                    print('before', arr2, i)
                    flip(arr,i)
                    print('after', arr2)
                    flip(arr,i+1) 
                    m = min(m, dp(i+1,arr ) + 1)
                    flip(arr,i+1)
                    flip(arr,i)
                
                flip(arr,i)
                for j in range(i+2,len(s1)):

                    flip(arr,j)
                    m = min(m, dp(i+1,arr) + x)
                    flip(arr,j)
                    #break

                flip(arr,i)

                return m

        s22 = bitt(s2)
        arr2 = bitt(s1)

        #print(bin(s22))
        #print(bin(arr2))

        @lru_cache(10_000)
        def dp2(i, arr):
            if i == len(s1):
                #print('eq', s22, arr)
                #print(bin(s22), bin(arr))
                if s22 == arr:
                    return 0
                else:
                    return float('inf')
            
            if s22 & (1 << i) == arr & (1 << i):
                return dp2(i+1, arr)
            else:
                
                #print(i, "not equal", s2, arr)
                m = float('inf')

                if i + 1 < len(s1):
                    #print('before', arr, bin(arr), i)
                    arr = flip(arr,i)
                    #print('after', arr, bin(arr),i)
                    arr = flip(arr,i+1) 
                    m = min(m, dp2(i+1,arr ) + 1)
                    arr = flip(arr,i+1)
                    arr = flip(arr,i)
                
                arr = flip(arr,i)
                for j in range(i+2,len(s1)):

                    arr = flip(arr,j)
                    m = min(m, dp2(j+1,arr) + x)
                    arr = flip(arr,j)
                    #break

                arr = flip(arr,i)

                return m    
        
        arr = [int(i) for i in s1]
        

        res = dp2(0, arr2) 

        return res if res != float('inf') else -1
