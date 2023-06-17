def  longest_subsequence(arr, k):

    dp = [0 for i in range(k + 1)]
    maxx = 0

    for num in arr:
        for i in range(k, num-1, -1):

            if i-num == 0:
                dp[i] = 1
            elif dp[i - num] > 0:
                dp[i] = max(dp[i], dp[i - num] + 1)

            maxx = max(dp[i], maxx)
    return maxx

arr = [2, 10, 6, 2, 2, 50000]
k = 10
val = longest_subsequence(arr, k)
# val - 3



class Solution:
    def idealArrays(self, n: int, mx: int) -> int:
        if mx == 1:
            return 1
        mod = 10 ** 9 + 7
        
        primes = set([2,3,5])
        for i in range(6, mx):
            for j in range(2, int(sqrt(i))+1):
                if i % j == 0:
                    break
            else:
                primes.add(i)
                    # break
        # print(primes)
        @lru_cache(None)
        def get_divisors(x):
            st = set([x])
            for i in range(2, int(sqrt(x))+1):
                if x % i == 0:
                    st.add(x//i)
                    st.add(i)
            return st
        
        @lru_cache(None)
        def dp(mx, l):
            if l == 1:
                return 1
            if mx == 1:
                return 0
            if l == 2:
                if mx in primes:
                    return 1
            if mx in primes:
                return 0
            res = 0
            divisors = get_divisors(mx)
            # print(mx, divisors)
            for d in divisors:
                res += dp(mx // d, l - 1)
                res %= mod
            return res
        
        @lru_cache(None)
        def dpp(n, j):
            return comb(n-1, j-1) % mod
        
        res = 1
        for i in range(2, mx+1):
            for j in range(1, 16):
                k = dp(i, j)
                # print(i, j, k)
                if n < j:
                    continue
                else:
                    k *= dpp(n, j)
                    k %= mod
                    res += k
                    res %= mod
        return res