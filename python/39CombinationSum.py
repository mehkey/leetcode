class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        candidates.sort()

        current = []

        def backtrack(i, candidates, target, current):
            
            if target < 0 :
                return
            
            if target == 0:
                res.append(current.copy())

            for j in range (i , len(candidates)):

                current.append(candidates[j])

                backtrack(j, candidates, target - candidates[j], current)

                current.pop()    

            return

        backtrack(0, candidates, target , current )
        return res
        