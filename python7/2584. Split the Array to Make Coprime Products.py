#import numpy as np

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        
 
        @cache
        def primeFactors(n):
     
            res = defaultdict(int)
            # Print the number of two's that divide n
            while n % 2 == 0:
                res[2] += 1
                n = n // 2

            # n must be odd at this point
            # so a skip of 2 ( i = i + 2) can be used
            for i in range(3,int(math.sqrt(n))+1,2):

                # while i divides n , print i ad divide n
                while n % i== 0:
                    res[i] += 1
                    n = n // i

            if n > 2:
                res[n] += 1
            
            return res

        prod_r = 1
        
        a = Counter()
        
        c = False
        
        for n in nums:
            
            r = primeFactors(n)
            for x in r:
                a[x] += r[x]

        prod_l = 1
        

        b = Counter()
        
        for i in range(0,len(nums)-1): 
            v = nums[i]
            
            r = primeFactors(v)
            
            
            
            for x in r:
                a[x] -= r[x]
                if a[x] == 0:
                    del a[x]


            for x in r:
                b[x] += r[x]
            

            c = False
            
            for x in a:
                if b[x] :
                    c = True
                    break
            
            if c == False:
                return i
            

        return -1


#import numpy as np

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        
        '''
        #a = np.array(nums)
        
        #prod_r = np.prod(a)
        
        @cache
        def primeFactors(n):
     
            res = defaultdict(int)
            # Print the number of two's that divide n
            while n % 2 == 0:
                res[2] += 1
                n = n // 2

            # n must be odd at this point
            # so a skip of 2 ( i = i + 2) can be used
            for i in range(3,int(math.sqrt(n))+1,2):

                # while i divides n , print i ad divide n
                while n % i== 0:
                    res[i] += 1
                    n = n // i

            # Condition if n is a prime
            # number greater than 2
            if n > 2:
                res[n] += 1
            
            return res

        prod_r = 1
        
        a = Counter()
        
        for n in nums:
            
            r = primeFactors(n)
            for x in r:
                a[x] += r[x]
            #for x in range(2, n+1):
            #    if n % x == 0: 
            #        a[x] += n // x
            #prod_r *= n
            #prod_r = gcd(prod_r,n)
            #print(prod_r)
        
        prod_l = 1
        
        #print(prod_r, prod_l)
        
        b = Counter()
        
        for i in range(0,len(nums)-1): #,v in enumerate(nums):
            v = nums[i]
            
            r = primeFactors(v)
            for x in r:
                a[x] -= r[x]
            
            #for x in primeFactors(v):
            #    b[x] += 1
            
            #r = primeFactors(v)
            for x in r:
                b[x] += r[x]
                
            #for x in range(2, v+1):
            #    if v % x == 0: 
            #        a[x] -= v // x
            
            #for x in range(2, v+1):
            #    if v % x == 0: 
            #        b[x] += v // x
            
            #print(v)
            #print(a)
            #print(b)
            
            if not a - b:
                return i
            
            #prod_r //= v
            #prod_l *= v
            
            #print(prod_r, prod_l)

            #if gcd(prod_r, prod_l) == 1:
            #    return i
            
            #prod_r = gcd(prod_r, v)
            #prod_l = gcd(prod_l, v)
            
            #print(prod_r, prod_l)
        
        return -1
        '''
        ans = 1
        for i, a in enumerate(nums[:-1]):
            for j, b in enumerate(nums[ans:], ans):
                if gcd(a, b) != 1:
                    ans = j
            if i == ans:
                return ans
        return -1

    def findValidSplit(self, nums: List[int]) -> int:
        freq = Counter()
        for x in nums: 
            for p in range(2, isqrt(x)+1): 
                while x % p == 0: 
                    freq[p] += 1
                    x //= p 
            if x > 1: freq[x] += 1
        ovlp = 0 
        prefix = Counter()
        for i, x in enumerate(nums): 
            if i <= len(nums)-2: 
                for p in range(2, isqrt(x)+1): 
                    if x % p == 0: 
                        if prefix[p] == 0: ovlp += 1
                        while x % p == 0: 
                            prefix[p] += 1
                            x //= p 
                        if prefix[p] == freq[p]: ovlp -= 1
                if x > 1: 
                    if prefix[x] == 0: ovlp += 1
                    prefix[x] += 1
                    if prefix[x] == freq[x]: ovlp -= 1
                if not ovlp: return i 
        return -1 