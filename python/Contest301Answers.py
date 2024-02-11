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



class Solution:
    def canChange(self, S: str, T: str) -> bool:
        def resolve(s):
            arr = []
            for i, c in enumerate(s):
                if c != '_':
                    arr.append([c, i])
            return arr
        arr = resolve(S)
        brr = resolve(T)
        if len(arr) != len(brr):
            return False
        for a, b in zip(arr, brr):
            if a[0] != b[0]:
                return False
            if a[0] == 'L':
                if a[1] < b[1]:
                    return False
            if a[0] == 'R':
                if a[1] > b[1]:
                    return False
        return True



def __init__(self):
        self.st = set([i for i in range(1, 1100)])

    def popSmallest(self) -> int:
        mn = min(self.st)
        self.st.remove(mn)
        return mn
        

    def addBack(self, num: int) -> None:
        self.st.add(num)


class Solution:
    def fillCups(self, A: List[int]) -> int:
        A.sort()
        if A[-1] >= A[0] + A[1]:
            return A[-1]
        # print(sum(A))
        return (sum(A) + (sum(A) % 2)) // 2


class SmallestInfiniteSet:

    def __init__(self):
        self.st = set([i for i in range(1, 1100)])

    def popSmallest(self) -> int:
        mn = min(self.st)
        self.st.remove(mn)
        return mn

    def addBack(self, num: int) -> None:
        self.st.add(num)
