class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        target = int(sum(nums) / len(nums))
        
        def cal(tar):
            t = 0
            for i,n in enumerate(nums):
                t += abs(tar-n) * cost[i]
            
            return t

        l = min(nums)
        r = max(nums)
        
        res = float("inf")
        
        m = float("inf")
        n = float("inf")
        
        while l <= r:
            
            mid = (l+r)//2
            
            res_mid = cal(mid)
            res_midm = cal(mid+1)
            res_midp = cal(mid-1)
            
            #print(res_mid)
            
            res = min(res,res_mid)
            
            if res_mid >= res_midm:
                l = mid + 1
            elif res_mid >= res_midp:
                r = mid - 1
            else:
                return res

        return res
