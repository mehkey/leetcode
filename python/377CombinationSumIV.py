class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        res = []
        
        current = []
        
        
        
        def backtrack( target , current , i  ):
            
            if target < 0 :
                return

            if target == 0 :
                res.append(current.copy())
                return

            for j in range( i, len(nums) ):
                
                current.append(nums[j])
                
                backtrack(target - nums[j], current, 0)
                
                current.pop()
            
            return

        backtrack(target, current, 0)
        
        return len(res)