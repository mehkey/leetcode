class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        
        #j = [i for i in range(0,n)]
        #print(j - i)
        
        #1 2 3 4
        
        """t = n * (n -1)  // 2 -1
        for i in range(0,n-1):
            print(nums[i])
            if nums[i] == nums[i+1] +1:
                print("here")
                t -= i + 1
        
        return t
        """
        #j = [nums[i] - i for i in range(n)]
        
        #print(j)
        
        c = Counter(j)
        #print(c)
        t = n * (n -1)  // 2 
        #t = 0
        #prev = 1
        #print(t)
        
        for j,v in c.items():
            #print(v)
            if v > 1:
                t -= v * (v - 1) //2

        #p = defaultdict(int)
        #for i in range(n-1):
            #for j in range(i+1,n):
            #print(nums[i],nums[i+1] - 1  )
            #if nums[i] == nums[i+1] - 1 :
                #print(prev)
            #    t -= prev
            #    prev += 1
            #else:
            #    prev -= 1
                
           # p.add(nums[i])

        return t
        