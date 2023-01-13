class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        p=10**9+7
        s=sum(nums)
        if s<2*k:
            return 0

        @cache
        def ct(i, k1, k2):
            n=nums[i]
            if i==len(nums)-1:
                ans=0
                if n>=k1 and k2==0:
                    ans+=1
                if n>=k2 and k1==0:
                    ans+=1
                return ans
            t1=max(k1-n, 0)
            t2=max(k2-n, 0)
            return (ct(i+1, t1, k2)+ct(i+1, k1, t2))%p

        return ct(0, k, k)



        n = len(nums)
        dp = [[0] * (k + 1)] + [[-1] * (k + 1) for _ in range(n)]
        dp[0][0] = 1
        def subsetSumCounts(s, idx):
            if s < 0:
            	return 0
            if dp[idx][s] < 0:
                dp[idx][s] = subsetSumCounts(s, idx - 1) + subsetSumCounts(s - nums[idx - 1], idx - 1)
            return dp[idx][s]
                
        invalid_pairs = sum([subsetSumCounts(i, n) for i in range(k)]) * 2
        return max(2**n - invalid_pairs, 0) % (10**9 + 7)