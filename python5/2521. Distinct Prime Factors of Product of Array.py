class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        total_product = 1
        
        for n in nums:
            total_product *= n
        
        count = 0

        m = max(nums)+1
        '''
        for i in range(2,m):

            start = True

            while total_product % i == 0:
                total_product //= i
                if start:
                    count+=1
                    start = False
        '''
        n = sorted(nums)
        
        s = list()
        for i in range(2,1000):
            found = False
            for c in s:
                if i % c == 0:
                    found = True
                    break
            if not found:
                s.append(i)

        #print(s)
        rem = set()
        res = 0
        for i in nums:
            for c in s:
                if i % c == 0 and c not in rem:
                    i //= c
                    rem.add(c)
                    res += 1
                
        
        return res