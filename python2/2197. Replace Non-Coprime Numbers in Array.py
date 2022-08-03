class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        
        
        def lcm(x, y):
            if x > y:
                greater = x
            else:
                greater = y

            while(True):
                if ((greater % x == 0) and (greater % y == 0)):
                    lcm = greater
                    break
                greater += 1

            return lcm
        
        if(len(nums)<=1):
            return nums
        #gc = [0] * (len(nums)-1)
        #nums.copy()
        #for i in range(len(nums)-1):
        #    if nums[]
        #    #gc[i] = gcd(nums[i],nums[i+1])
        """i = 0
        while True:
            
            g = gcd(nums[i],nums[i+1])
            if g > 1:
                l = lcm(nums[i],nums[i+1])
                del nums[i]
                nums[i] = l
                #del nums[i+1]

            else:
                i+=1
                
            if i >= len(nums) -1 :
                break
                
        return nums
        
        res = []
        for num in nums:
            while res and gcd(res[-1], num) > 1:
                num = lcm(res[-1], num)
                res.pop()
            res.append(num)
        return res
        """
        res = []
        for a in nums:
            while True:
                x = math.gcd(res[-1] if res else 1, a)
                if x == 1: break # co-prime
                a = a * res.pop() // x
                print(a)
            res.append(a)
            print(res)
        return res
        #print(gc)
        #return res