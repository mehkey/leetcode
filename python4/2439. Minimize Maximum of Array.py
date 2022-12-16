class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        #m = min(nums)
        #mm = max(nums)
        
        #for i in range(m,mm+1):
        '''res = defaultdict(int)
        
        res[nums[0]] = 1

        for i in range(1,len(nums)):

            n = nums[i]

            res[n] += 1

        
        return 
        
        '''
        cum_sum = maximum = 0

        for i, num in enumerate(nums, start=1):
            cum_sum += num
            print(cum_sum)
            print(ceil(cum_sum / i))
            maximum = max(ceil(cum_sum / i), maximum)

        return maximum
            
        
        
        '''
        n = len(nums)
        t = sum(nums)
        G = defaultdict(list)
        self.components = 0
        for v, w in edges:
            G[v].append(w)
            G[w].append(v)
        def dfs(v, t, visited):
            if v in visited: return 0
            visited.add(v)
            res = nums[v]
            for w in G[v]:
                res += dfs(w, t, visited)
            if res == t:
                self.components += 1
            return res if res != t else 0
        for i in range(n, 1, -1):
            if not t % i:
                self.components = 0
                dfs(0, t//i, set())
                if self.components == i:
                    return i - 1
        return 0
        '''