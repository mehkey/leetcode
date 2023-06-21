class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        """
        
        [1,2,3]
        
        
        [[]]
        
        
        index 0 ADD [1] [2] [3]
        
        
        [[],[1],[2],[3]]
        
        
        [[],[1],[2],[3],[1,2],[1,3]]  ADD current:[1] add [1,2],[1,3] index 1
        
        ADD [1,2,3] current:[1,2] add [1,2,3] index 2
        
        ADD [1,3,2] current:[1,3] add [1,3,2] index 2

        [[],[1],[2],[3],[1,2,3],[1,3],[1,3,2]]
        
        
        """
        
        """
        def dfs(cur,i):

            if i == len(nums) - 1:
                return cur

            res = [[]]
            for j in range(i,len(nums)):

                for c in cur:
                    if c:
                        res.append(c.append(nums[j]))
                    else:
                        res.append([nums[j]])
            cur.extend(res)
            dfs(cur, i+1)
            
            return cur
        

        res = []
        
        def dfs(cur, i):

            res.append(cur)
            
            if i == len(nums)  :
                return cur.copy()
            
            
            for j in range(i,len(nums)):
                
                newcurrent = cur + [nums[j]] if len(cur) > 0 else [nums[j]]
      
                dfs(newcurrent , j+1)

            return res

        return dfs([],0)

        """

        
        
        