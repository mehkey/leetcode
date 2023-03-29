class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        primes = []

        for num in range(2, 1000):

            for i in primes:
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
        
        print(len(primes))
        primes = [0] + primes

        previous_min = 0
        
        for n in nums:

            if n <= previous_min:
                return False
            
            min_next_number = 0
            for p in primes:
                if p < n:
                    if n - p > previous_min:
                        min_next_number = n-p
                else:
                    break
            previous_min = min_next_number
        return True