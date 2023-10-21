class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        
        
        #def dp()
        
        min_index = 0
        min_val = float('inf')
        
        for i,n in enumerate(nums):
            if n < min_val:
                min_val = n
                min_index = i

        res = 0
        
        #print(min_val)
        s = set()
        
        for c in range(len(nums)):
            
            if len(s) == len(nums):
                return res
            
            res += x if c > 0 else 0
            
            for cc in range(len(nums)):
                if cc not in s and nums[cc]  < (nums[cc+1] if cc+1 <len(nums) else nums[0]) + x :
                    #print(cc, nums[cc], x * c )
                    res += nums[cc] 
                    s.add(cc)
            
            temp = nums[-1]
            for i in range(len(nums)-1,0,-1):
                nums[i] = nums[i-1]
            nums[0] = temp
            #print(nums)
        return res

        n = len(A)
        res = [x * k for k in range(n)]
        for i in range(n):
            cur = A[i]
            for k in range(n):
                cur = min(cur, A[i - k])
                res[k] += cur
        return min(res)