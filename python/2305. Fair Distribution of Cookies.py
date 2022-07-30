class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        """
        res = []
        
        def dfs(cur, i):

            if len(cur) == k:
                res.append(cur)
                return cur.copy()
            
            if i == len(nums)  :
                #res.append(cur)
                return cur.copy()
            
            
            for j in range(i,len(nums)):
                
                newcurrent = cur + [nums[j]] if len(cur) > 0 else [nums[j]]
      
                dfs(newcurrent , j+1)

            return res

        dfs([],0)
        
        print(res)
        
        return min([sum(res[i]) for i in range(len(res))])
        
        """
        
        children = [0] * k
        result = float('inf')
        
        if len(cookies) <= k:
            return max(cookies)

        def recurse(i, children):
            #print(children)
            if i == len(cookies):
                nonlocal result
                result = min(result, max(children))
                return

            cookie_size = cookies[i]
            for child in range(k): # min(i + 1, k) important for avoiding TLE
                children[child] += cookie_size
                recurse(i + 1, children)
                children[child] -= cookie_size

        recurse(0, children)

        return result
    
"""
    
class Solution:
    def distribute(self, cookies, i, n, k, buckets):
        if i >= n:
            self.minmax = min(self.minmax, max(buckets))
            return
        for j in range(k):
            buckets[j] += cookies[i]
            self.distribute(cookies, i + 1, n, k, buckets)
            buckets[j] -= cookies[i]

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        if n == k:
            return max(cookies)
        buckets = [0] * k
        self.minmax = float('inf')
        self.distribute(cookies, 0, n, k, buckets)
        return self.minmax
"""