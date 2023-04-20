class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        primes = set()
        
        '''
        def isPrime(n):
            #if n <= 1:
            #    return False

            for i in range(2, 4*10**6 ):#2, int(n/2)+1):
                for p in primes:
                    if i % p == 0:
                        break
                else:
                    primes.add(i)
            
            return True
        '''
        def isPrime(n):
            if n < 2:
                return False
            i = 2
            while i*i <= n:
                if n / i == 0:
                    return False
                i += 1
            return True
        
        isPrime(0)
        
        M = len(nums)
        #M = len(nums[0])
        
        #print(isPrime(883))
        #print(isPrime(985))
        m = 0
        
        for i in range(M):
            for j in range(M):
                #print(i,j,M - 1 -j)
                if i == j or i == M - 1 -j:
                    #print(i,j)
                    
                    if isPrime(nums[i][j]): 
                        m = max(m,nums[i][j])
        
        return m