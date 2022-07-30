class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        
        """h = []
        
        
        
        #total = 1
        h.append((delay+1,0))
        h.append((forget+1,1))

        total = 0
        nu = 1
        
        for i in range(2,n+1):
            #print("i",i)
            
            #print(h)
            #print("active total", total)
                
            while h and h[0][0] == i:

                p = heapq.heappop(h)
                #print("HERE")
                if p[1] == 0:
                    total += 1
                else:
                    nu -= 1
                    total -= 1
            #print(h)
            #print("active total", total)
            for j in range(total):
                nu += 1
                heapq.heappush(h,(i+delay,0))
                heapq.heappush(h,(i+forget,1))
            #print("active total", total)
            #print("person ", nu)
        
        #for p in h:
        #    if p[1] == 0:
        #        total += 1
    
        return nu #nu - total -1
        
        """
        MOD = int(1e9 + 7)
        
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2, n+1):
            spawn = dp[max(i-delay,0)] - dp[max(i-forget,0)]
            dp[i] = (dp[i-1] + spawn)%MOD
        return (dp[n] - dp[max(n-forget,0)])%MOD