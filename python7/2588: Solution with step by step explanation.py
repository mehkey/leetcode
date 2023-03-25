class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        pre_xor = [0] * (n+1)
        pre_xor[0]=0
        cnt = [0]*(1<<20)
        cnt[0] = 1
        
        for i in range(1,n+1):
            pre_xor[i] = pre_xor[i-1] ^ nums[i-1]
            res += cnt[pre_xor[i]]
            cnt[pre_xor[i]] += 1

        return res