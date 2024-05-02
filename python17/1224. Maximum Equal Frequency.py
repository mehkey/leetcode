class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        
        cnt,freq,maxF,res = collections.defaultdict(int), collections.defaultdict(int),0,0



        for i,num in enumerate(nums):
            cnt[num] += 1
            freq[cnt[num]-1] -= 1
            freq[cnt[num]] += 1
            print(freq)
            maxF = max(maxF,cnt[num])
            if maxF*freq[maxF] == i or (maxF-1)*(freq[maxF-1]+1) == i or maxF == 1:
                res = i + 1
        return res


        l = 0
        r = 0
        
        res = 1
        
        def cal(dis):
            
            c = Counter()
            
            #keys = set()
            
            for i in range(dis):
                c[nums[i]] += 1
            
            diff = 0
            
            
        while l <= r:
            
            mid = (l+r) // 2
            
            if cal(mid):
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid -1
        
        return res
        
        '''
        res = 1
        
        
        #c = Counter(nums)
        
        N = len(nums)
        l = 0
        
        c = Counter()
        
        def cal(c):
            
            K = len(c.keys())
            
            for 
            
            
        for r in range(N):
            
            c[nums[r]] += 1

            while l <= r and cal(nums) :

                res = max(res, r - l + 1)

                c[nums[l]] -= 1

                if c[nums[l]] == 0:
                    del c[nums[l]] 

                l+= 1

        return res
        '''