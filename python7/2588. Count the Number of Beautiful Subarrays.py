def beautifulSubarrays(self, A):
        dp = Counter({0: 1})
        res = pre = 0
        for a in A:
            pre ^= a
            res += dp[pre]
            dp[pre] += 1
        return res
ctr = Counter(accumulate(nums, xor, initial = 0))

        return sum (n*(n-1) for n in ctr.values())//2