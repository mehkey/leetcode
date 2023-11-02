class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:

        '''

        110
        101

        111
        100

        11011001
        10110100
        11111101
        10010000

        '''
        #nums.sort()

        #for i in range(n):

        d = defaultdict(int)
        
        for n in nums:
            for i in range(32):
                if (1<<i) & n:
                    d[i] += 1
        t = 0
        
        for i in range(k):
            cur = 0
            for i in range(32):
                if d[i]:
                    cur += (1<<i)
                    d[i] -= 1
            
            t += (cur ** 2)
            t %= 10**9 + 7

        return t
        
        

        '''
        def dp(i):
            if i == len(nums):
                t = 0
                for j in range(k):
                    t += nums[j]**2
                return t
        1010
        1100
        
        0010
        1001
        '''

        