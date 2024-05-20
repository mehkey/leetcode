class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        @cache
        def dp(n, k):
            if k == 0: return 1
            if n == 1 or k < 0: return 0
            return dp(n, k-1) + dp(n-1, k) - dp(n-1, k-n)
        return dp(n, k) % (10**9+7)
        
        def dfs(i, remain):
            # base 1
            if remain < 0:
                return 0

            # base 2
            if i == 0:
                return 1 if remain == 0 else 0 

            # seen before
            if (i, remain) in memo:
                return memo[(i, remain)]

            # A: f(n, k) = f(n − 1, k) + f(n − 1, k − 1) + f(n − 1, k − 2) + ⋯ + f(n − 1, k − n + 1)
            # B: f(n, k − 1) = f(n − 1, k − 1) + f(n − 1, k − 2) + f(n − 1, k − 3)+ ⋯ + f(n − 1, k − n + 1) + f(n − 1, k − n)
            # A - B : f(n , k) = f(n − 1, k) + f(n, k − 1) − f(n − 1, k − n)

            # case 1; ith number does not create inverse pair
            # so we only have to search within [1,.., i - 1]
            skip = dfs(i - 1, remain)

            # case 2; ith number create inverse pair
            # so we only have to search within [1,.., i]
            pick = dfs(i, remain - 1)

            # case 3; gap beween case1 and case 2
            gap = 0
            if remain >= i:
                gap = dfs(i - 1, remain - i)

            memo[(i, remain)] = (skip + pick - gap) % kMod

            return memo[(i, remain)]

        kMod = 10 ** 9 + 7

        # memo [(i, remain)] := total num of after adding the ith number to i-1 numbers in all places if remain inverse pairs needs to be created
        memo = dict()

        return dfs(n, k)

        N = n
        M = 10**9+7

        @cache
        def dp(i,left, k):
            if left == 0:
            #if i == N + 1:
                if k == 0:
                    return 1
                return 0

            res = 0

            for j in range(1, N + 2):
                if k - max(0,i - j) >= 0:
                    res += dp( max(i,j) + 1, left-1,k - max(0,i - j) )

            return res

        return dp(1, n,  k) % M
