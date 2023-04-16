class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        cnt = Counter(nums)
        
        def count(arr):
            if not arr:
                return 1
            arr1 = [x for x in arr if math.gcd(x, arr[0]) == 1]
            return (count(arr[1:]) + cnt[arr[0]] * count(arr1)) % MOD

        candidates = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]
        return (count(candidates) * pow(2, cnt[1], MOD) - 1) % MOD
    

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        sq = {4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28}
        
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        dic = {}
        for i in nums:
            if i in sq:
                continue
            tmp_dic = dict(dic)
            for k in dic.keys():
                if gcd(k, i) == 1:
                    cur = k * i
                    if cur in tmp_dic:
                        tmp_dic[cur] += dic[k]
                    else:
                        tmp_dic[cur] = dic[k]
            if i in tmp_dic:
                tmp_dic[i] += 1
            else:
                tmp_dic[i] = 1
            dic = tmp_dic
        # print(dic)
        return sum([dic[k] for k in dic.keys()]) % (10**9 + 7)
    

    class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        candidates = set([2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30])
        cnt = defaultdict(int)
        for num in nums:
            if num in candidates:
                cnt[num] += 1
        
        def count(arr):
            if not arr:
                return 1
            arr1 = []
            for num in arr[1:]:
                if math.gcd(num, arr[0]) == 1:
                    arr1.append(num)
            return (count(arr[1:]) + cnt[arr[0]] * count(arr1)) % MOD
            
        ones = nums.count(1)
        tmp = 1
        for _ in range(ones):
            tmp = (tmp * 2) % MOD
        return (count(list(cnt)) * tmp - 1) % MOD
    

    class Solution:
    def squareFreeSubsets(self, nums):
        # Pre-prepared bitmask
        valid = {1:0, 2:1, 3:2, 5:4, 6:3, 7:8, 10:5, 11:16, 13:32, 14:9, 15:6, 17:64, 19:128, 21:10, 22:17, 23:256, 26:33, 29:512, 30:7}
        count = defaultdict(int)
        for n in nums:
            if n in valid:
                for k in count.copy():
                    # If n & subset with bitmask k have common prime factor
                    if valid[n] & k == 0:
                        # Since the subset is still valid taking n in, we now have count[k] more subsets
                        # count[k] subsets without n and count[k] subsets with n
                        count[valid[n]|k] += count[k]
                # subset {n}
                count[valid[n]] += 1
        return sum(count.values()) % (10 ** 9 + 7)


class Solution:
    def squareFreeSubsets(self, nums):
        n = len(nums)

        primes = [2,3,5,7,11,13,17,19,23,29]

        dp = [0]*(1<<10)

        dp[0] = 1

        for num in nums:
            mask = 0
            for i,p in enumerate(primes):
                if num%(p*p) == 0:
                    mask = -1
                    break
                if num%p == 0:
                    mask = mask|(1<<i)

            if mask >= 0:
                for i in range(1<<10):
                    if i&mask == 0:
                        dp[i|mask] += dp[i]

        return (sum(dp)-1)%(10**9+7)