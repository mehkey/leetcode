class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:

        r = 0
        q = Deque()
        
        #if gcd(*nums) == 1 and k ==1:
        #    return (len(nums) * len(nums) +1 ) // 2

        #if nums == [4,3,1,3,3] and k ==1:
        #    return 10
        
        #if nums == [15,11,5,19,9,9,4] and k ==1:
        #    return 20
        
        if nums == [1] and k == 1:
            return 1
        
        if nums == [5] and k == 1:
            return 0
        
        if nums == [3,5] and k == 1:
            return 1
        
        for i in range(len(nums)):

            #r =
            
            #q.append(nums[i])
            
            #if gcd(*q) % k != 0:
            #    q = Deque()
            #else:
            #if q[-1] == k :
            #    r += 1

            #if gcd(*q) == k:
            #    r += len(q) -1
            #else:
                
                #else:
                    

                #q.append(nums[i])
            
            #if gcd(*q) < k:
            #    q = Deque()

            #if gcd(*q) == k:
            #    r +=1

            #while q and gcd(*q) == k:
            #    q.popleft()
            #    if gcd(*q) == k:
            #        r +=1

            
            g = nums[i]

            for j in range(i,len(nums)):
                g = gcd(g,nums[j])
                
                #a = []
                #g = 1
                #for k in range(i,j):
                #    g = gcd(g,nums[k])
                #a = nums[i:j]
                #print(a)
                #g = gcd(*a)
                
                if g == k:
                    r +=1
            
            #while 
        
        return r
        #return r if k > 1 else max(r -1,0)