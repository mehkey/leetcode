class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        
        '''
        
        [5,7,1,3]
        
        [101,111,1,11]


        '''


        #acc = accumulate(nums, lambda x,y: x&y)

        #print(list(acc))
        '''
        cur = nums[0]
        for n in nums:
            cur &= n
        
        if cur == 0:
            count = 1
            mm = cur
            for i in range(0,len(nums)):

                n = nums[i]

                cur &= n
                if cur == mm:
                    if i+1 < len(nums):
                        cur = nums[i+1]
                        count += 1
            return count if cur == mm else count -1
        else:
            return 1
        '''
        sum_scores = 0

        cur = nums[0]

        for n in nums:
            cur &= n
            #print(bin(n)[2:])

        #print(cur)
        #print(bin(cur)[2:])
        
        if cur > 0:
            return 1
        
        mm = cur

        cur = nums[0]
        count = 1

        
        for i in range(0,len(nums)):

            n = nums[i]

            cur &= n

            if cur == mm:
                if i+1 < len(nums):
                    cur = nums[i+1]
                    count += 1

        return count if cur == mm else count -1


        