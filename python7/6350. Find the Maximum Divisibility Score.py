class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        
        s = -1
        v = 0
        
        #divisors = set(divisors)
        
        for d in divisors:
            cur = 0
            for n in nums:
                            
                if n % d == 0:
                    cur += 1
            
            #print(d, cur)
            if cur > s:
                s=cur
                v = d
            elif cur == s and d < v:
                s = cur
                v = d
        
        return v