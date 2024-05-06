class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = c[: 2]
        return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in c)

        dx = c[1][0] - c[0][0]
        dy = c[1][1] - c[0][1]
        
        #a= b*X + Y
        if dy == 0:
            print('dy0')
            return True

        N = len(c)
        c0 = c[0][0]
        c1 = c[0][1]
        #print(dy)
        tar = c0 - c1*dx/dy
        #print(tar)
        #print(dx/dy)
        for i in range(2,N):
            c2 = c[i][0]
            c3 = c[i][1]
            if c2 != c3* (dx/dy) + tar: #c2 * dx - c3 * dy != -dy:
                return False
            #print( c2 * dx - c3 * dy )
        
        
        return True