
from sortedcontainers import SortedList

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        hm = defaultdict(int)

        l = 0
        N = len(arr)
        res = 0
        for r,n in enumerate(arr) :

            hm[arr[r]] = max(hm[arr[r]], hm[arr[r]  - difference] + 1)

            res = max(res, hm[arr[r]] )


        return res
        '''
        hm = defaultdict(int)
        
        for n in arr:
            hm[n] = 1
        
        #chm = {}
        chm = SortedList()
        
        
        l = 0
        
        res = 0
        
        def check(hm):
            
            #def dfs(node):
            for i in range(len(hm)-1):
                if hm[i+1] - hm[i] > difference:
                    return False
            
            return True
        
        for r in range(len(arr)):
            
            #chm[arr[r]] += 1
            chm.add(arr[r])

            
            while l <= r and not check(chm):
                
                #chm[arr[l]] -= 1
                #if chm[arr[l]] == 0:
                #    del chm[arr[l]]
                chm.remove(arr[l])
                l += 1
            res = max(res, r - l + 1)
            
        return res
        '''