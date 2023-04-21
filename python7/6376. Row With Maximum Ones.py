class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
        c = 0
        ro = 0
        
        for r in range(len(mat)):
            cur = sum(mat[r])
            
            if cur > ro:
                c = r
                ro = cur
        
        return [c,ro]
            