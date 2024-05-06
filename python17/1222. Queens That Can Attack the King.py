class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        
        cx= king[0]
        cy= king[1]
        
        #q = set(queens)

        res = []
        
        def change(cx, cy , dx, dy):
            
            while 0 <= cx < 8 and 0 <= cy < 8:
                cx += dx
                cy += dy

                if [cx,cy] in queens:
                    return [cx,cy]
            return []
        
        for dx,dy in [ [1,0], [-1,0], [0,-1], [0,1], [1,1],[1,-1],[-1,-1],[-1,1]]:
            cur = change(cx,cy,dx,dy)
            if cur:
                res.append(cur)
            
        return res
