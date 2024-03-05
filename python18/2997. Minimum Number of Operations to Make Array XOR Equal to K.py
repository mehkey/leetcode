class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        X = 0
        for n in nums:
            X ^= n
        x0 = X
        x1 = k

        s = 0
        while x0 or x1:
            if x0 &1 != x1 &1:
                s += 1
            
            x0 >>= 1
            x1 >>= 1
        
        return s