class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        
        
        nums.sort()

        N = len(nums)
        c = 0
        s = 0
        
        left_diff = {}
        right_diff = {}
        for i,v in enumerate(nums):
            left_diff[i] = c * v - s
            c += 1
            s += v

        nn = nums[::-1]

        c = 0
        s = 0
        
        for i,v in enumerate(nn):
            right_diff[N-i-1] = s -  c * v 
            c += 1
            s += v


        res = []
        
        for q in queries:
            index_q = bisect_left(nums,q)

            if index_q < N:
                res.append(left_diff[index_q] + right_diff[index_q]  + (N - index_q) * abs(nums[index_q]-q)  - index_q * abs(nums[index_q]-q) )
            else:
                res.append( max(left_diff.values()) + N * ( q - nums[-1] ) )
                           
        return res