class Solution:
    def distinctSequences(self, n: int) -> int:
        """mod = 10**9 + 7
        dp, dp2 = {(7, 7): 1}, Counter()
        for _ in range(n):
            for i, j in dp:
                for k in range(1, 7):
                    if k != i and k != j and gcd(j, k) == 1:
                        dp2[j, k] = (dp2[j, k] + dp[i, j]) % mod
            dp, dp2 = dp2, Counter()
        return sum(dp.values()) % mod
        
        """
        @cache
        def f(i,a,b):
            if i==0:return 1
            ans=0
            for j in range(1,7):
                if (j not in (a,b)) and (b==-1 or gcd(j,b)==1):
                    ans+=f(i-1,b,j)
            return ans%(10**9+7)
        
        return f(n,-1,-1)



        g=set()
          for i in range(1,7):
               for j in range(1,7):
                    if gcd(i,j)==1:
                        g.add((i,j))
                        
          @cache
          def dfs(n,i1,i2):
              if n==0:
                    return 1
                
              ans=0
              for j in range(1,7):
                  if j!=i1 and j!=i2 and (i2==-1 or (i2,j) in g):
                      ans+=dfs(n-1,i2,j)
              return ans
        
          return dfs(n,-1,-1)%(10**9+7)


mod=1000000007
@cache
def func(n,prev,pp):
    if n==0:
        return 1
    ans=0
    for i in range(1,7):
        if prev==-1:
            ans+=func(n-1,i,prev)
            ans=ans%mod
        elif pp==-1:
            if(math.gcd(i,prev)==1 and i!=prev):
                ans+=func(n-1,i,prev)
                ans=ans%mod
        else:
            if(math.gcd(i,prev)==1 and i!=prev and i!=pp):
                ans+=func(n-1,i,prev)
                ans=ans%mod
    return ans;
class Solution:
    
            
    def distinctSequences(self, n: int) -> int:
        return func(n,-1,-1)



class Solution:
    def distinctSequences(self, n: int) -> int:
        mod = 10 ** 9 + 7
        
        @cache
        def dp(n, prev, twoprev):
            if n == 0:
                return 1

            total = 0
            for i in range(1, 7):
                if prev is not None:
                    if gcd(i, prev) == 1:
                        if twoprev is not None:
                            if twoprev != i and prev != i:
                                total += dp(n - 1, i, prev) % mod
                        else:
                            if prev != i:
                                total += dp(n - 1, i, prev) % mod
                else:
                    total += dp(n - 1, i, prev) % mod
            
            return total
        
        return dp(n, None, None) % mod