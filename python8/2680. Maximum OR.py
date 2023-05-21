class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        

        cur = 0
        saved = 0
        for num in nums:
            saved |= num & cur
            cur |= num
        
        max_num = 0
        
        for num in nums:
            max_num = max(max_num, saved | (cur & ~num) | num << k)
        return max_num


        '''
        
        
        

        nums.sort()
        
        l=0
        r=len(nums)-1
        
        while l<=r:
            
            mid = (l+r)//2
            
            
        
        c = []
        l = 0
        
        #r = 

        for n in nums:
            b = bin(n)[2:]

            if len(b) > l:
                c = []
                l = len(b)
                c.append(b)
            elif len(b) == l:
                c.append(b)

        #c.append(a)
        
        #print(c)
        
        if len(c) == 1:
            o = 0
            for n in nums:
                if n!=c[0]:
                    o|=n
            return c[0] | o
        
        else:
            m = 0
            nn = 0
            for n in c:
                cur = n[2:]
                if cur > int(m, 2):
                    m = cur
                    nn = n
            
            o = 0
            for n in nums:
                if n!=nn:
                    o|=n
            return nn | o
            

        
        #print(9*2|12)
        
        #print(12*2|9)
        
        #print(bin(9*2|12)[2:])
        #print(bin(12*2|9)[2:])
        
        #print(9*2|12)
        
        #print(12*2|9)
        
        #return 0
        '''