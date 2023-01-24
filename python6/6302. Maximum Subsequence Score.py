class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        nums = []
        
        for x, y in zip(nums1, nums2):
            nums.append((x, y))
            
        nums.sort(key=lambda x: -x[1])
        
        h = []
        best = 0
        total = 0
        for x, y in nums:

            heapq.heappush(h, x)
            total += x
            
            if len(h) > k:
                t = heapq.heappop(h)
                total -= t
                
            if len(h) == k:
                print(total, y)
                best = max(best, total * y)
            
        return best

        '''
        nn = len(nums1)
        
        arr = []
        
        for i,n in enumerate(nums1):
            arr.append((-max(nums2[i]*k,n),-nums2[i],-n,i))
        
        heapify(arr)
        
        res = 0
        m = float('inf')
        su = 0
        
        min1 = float('inf')
        min2 = float('inf')
        
        for i in range(k):
            p = heappop(arr)
            #print(p[1],p[2])
            p = (p[1],p[2],p[3])

            su += -p[1]

            m = min(m,-p[0])
            
            #heappush(mm,-p[0])
            
            res = su * m
        
        return res
            
        
        arr = []
        
        for i,n in enumerate(nums1):
            arr.append((1 if nums2[i] == 0 else 0 ,-n,-nums2[i],i))

        heapify(arr)
        
        res = 0
        m = float('inf')
        su = 0
        
        min1 = float('inf')
        min2 = float('inf')
        
        #mini = float('inf')
        #arr2 = []
        mm = []
        
        for i in range(k):
            p = heappop(arr)
            p = (p[1],p[2],p[3])
            if -p[1] == min2 and  -p[0] < min1:
                min2 = -p[1] 
                min1 = -p[0]
                
            if -p[1] < min2:
                min2 = -p[1] 
                min1 = -p[0]
                
            su += -p[0]
            
            #mini = min(mini,-p[0])
            #heappush(arr2,(p[1],))
            
            m = min(m,-p[1])
            heappush(mm,-p[1])
            
            res = su * m
        
        #print(min1,min2)
        #print(mm)
        
        print(arr)
        #if len(mm) >1:
        heappop(mm)
        if len(mm) == 0:
            mmm = float('inf')
        else:
            mmm = mm[0]
        su -= min1
        
        while arr:
            p = heappop(arr)
            p = (p[1],p[2],p[3])
            su += -p[0]

            oldm = m
            
            m = min(mmm,-p[1])
            
            res = max(res,su*m)

            m = oldm
            su += p[0]
                
        
        return res
        
        #for n in nums2:
        
        '''
            