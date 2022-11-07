class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:

        def create(m):
            t = 0
            for n in m:
                if m[n] > 0:
                    t = t | (1 << n)
            return t
        
        def add(a,m):
            ans = bin( a )
            s = str(ans)[2:]
            for i, b in enumerate( s[::-1]):
                if b == '1':
                    m[i] += 1

        def remove(a,m):
            ans = bin( a )
            s = str(ans)[2:]
            for i, b in enumerate( s[::-1]):
                if b == '1':
                    m[i] -= 1
        
        res = []

        
        n = defaultdict(int)
        for i in nums:
            add(i,n)

        cur = 0

        
        
        m = defaultdict(int)
        r = 0
        c = 0
        o = 0

        for i,v in enumerate(nums):

            o = create(n)
            
            while r < len(nums) and (create(m) != o or (c==0 and nums[i] ==0)):
                add(nums[r],m)
                r+=1
                c+=1

            res.append(c)

            remove(nums[i],m)
            remove(nums[i],n)
            c-=1

        return res
        

        

        
        
