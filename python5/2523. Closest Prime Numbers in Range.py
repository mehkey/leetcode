class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        s = list()
        hm = defaultdict(int)
        ind = 0
        for i in range(2,min(100000,right+1)):
            found = False
            for c in s:
                if i % c == 0:
                    found = True
                    break
            if not found:
                s.append(i)
                hm[i] = ind
                ind +=1

        start = left
        while start not in hm:
            start+=1

        end = right
        while end not in hm:
            end-=1

        if start >= end:
            return [-1,-1]
        d = float("inf")
        f,e = 0,0

        for i in range(hm[start], hm[end]):

            if s[i+1]-s[i] < d:
                d =s[i+1]-s[i]
                f = s[i]
                e = s[i+1]

        return [f,e]

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True for i in range(right+1)]
        prime[1] = False
        def primeNum(n):
            p = 2
            while (p * p <= n):
                if (prime[p] == True):
                    for i in range(p * p, n+1, p):
                        prime[i] = False
                p += 1
        first,second = -1,-1
        diff = math.inf
        ans = [-1,-1]
        primeNum(right)
        for num in range(left,right+1):
            if prime[num] and first == -1:
                first = num
            elif prime[num] and second == -1:
                if diff > num - first:
                    diff = num - first
                    ans = [first,num]
                    first,second = num,-1
                else:
                    first = num
            else:
                continue
        if ans[0] == -1 or ans[1] == -1:
            return [-1,-1]
        else:
            return ans