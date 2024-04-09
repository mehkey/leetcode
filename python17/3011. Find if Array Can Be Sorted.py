class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        '''
        prev = nums[0]
        N = len(nums)
        for i in range(1,N):
            print(prev,nums[i])
            if prev <= nums[i] :
                prev = nums[i]
            elif prev.bit_count() == nums[i].bit_count():
                #print('H',prev.bit_count(),nums[i].bit_count()  )
                prev = max(nums[i], prev)
            else:
                return False
        
        
        return True
        '''

        gk = nums[0].bit_count()
        cma = 0
        cmi = inf
        
        pma = 0

        for n in nums:

            if n.bit_count() == gk:
                if n < pma:
                    return False
                cma = max(cma,n)
            else:
                
                pma = cma
                
                if n < pma:
                    return False

                cma = n
                gk = n.bit_count()

        return True
        
        
        groups = groupby(nums, lambda x: x.bit_count())


        for c in groups:
            k,v = c

            v= list(v)

            m = max(v)
            mi = min(v)
            
            if mi < pma:
                return False
            
            pma = m
        
        return True
            