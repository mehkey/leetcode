class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        mod = 10**9 + 7
        
        m = 1
        
        t = 0

        while m <= n:
            m *=2 % mod
            t += 1
        

        t -= 1
        
        arr = []
        while n > 0:
            while m > n:
                m //= 2
            arr.append(int(m) % mod)
            n -= m
        
        arr.reverse()
        
        res = []
        
        for q in queries:
            
            p = 1
            for i in range(q[0],q[1] + 1):
                p = (p * arr[i]) % mod
            res.append(p)
        
        return res