class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
        '''tot = 0
        
        for n in nums:
            
        '''
        res = []
        
        '''def dfs(cur, i):

            res.append(cur)
            
            if i == len(nums)  :
                return cur.copy()
            
            
            for j in range(i,len(nums)):
                
                newcurrent = cur + [nums[j]] if len(cur) > 0 else [nums[j]]
      
                dfs(newcurrent , j+1)

            return res

        dfs([],0)
        '''
        
        res = []
        n = len(nums)
        for r in range(0,n+1):
            for l in range(0,r):
                #print(l,r)
                res.append( nums[l:r] )
        
        #print(res)
        tot = 0
        #res = set(())
        for nn in res:
            tot += len(set(nn)) ** 2
        return tot