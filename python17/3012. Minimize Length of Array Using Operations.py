class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        
        '''
        if len(nums) == 1:
            return 1

        if gcd(*nums) > 1:
            return 2
        else:
            return 1
        '''
        
        #nums.sort()
        if len(nums) <= 2:
            return 1

        m= min(nums)
        g = gcd(*nums)
        c = Counter(nums)
        for x in nums:
            if x % m != 0:
                return 1
        #print(m,c,c[m] // 2)
        return max(1, ceil(c[m]/2))
        return max( (c[m]+1)//2 ,1)