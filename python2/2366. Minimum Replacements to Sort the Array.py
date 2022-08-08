class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        n = len(nums)
        cur = nums[-1]
        res = 0
        for i in range(len(nums)-2,-1,-1):
            
            if nums[i] <= cur:
                cur = nums[i]
                continue
            else:
                k = ceil(nums[i] / cur)
                
                res += k -1
                
                cur = nums[i] // k
                
                #print("nums[i]", nums[i])
                
                #if k %1 == 0.0:
                    #print('er')
                #    res += k - 1
                #    cur = nums[i] // (math.ceil(k))
                #else:
                    
                #    res += (math.ceil(k))
                    #print(math.floor(k)-1 )
                    #print(2)
                    #print(nums[i] % cur + cur) 
                    #cur =  (nums[i] - (math.floor(k) -1) * cur) // 2
                #    cur = nums[i] // (math.ceil(k))

        return int(res)
        """
        
        n = len(nums)
        ret = 0
        prev = nums[ - 1]
        for ind in range(n - 2, -1, -1):
            num = nums[ind]
            
            k = ceil(num / prev)
            #print("k",k)

            ret += k - 1
            #print("k-1",k-1)
            prev = num // k
            #print("prev",num // k)

        return ret
        """