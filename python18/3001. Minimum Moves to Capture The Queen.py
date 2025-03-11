class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:

        for direction in [[1,0],[-1,0],[0,1],[0,-1]]:
            dx, dy = direction
            for i in range(1,8):
                # if we spot bishop just break, because the rook may be in a blind spot to queen. no need to check further
                if e + i*dx == c and f + i*dy == d:
                    break
                # if we spot rook , we can capture queen in 1 move
                if e + i*dx == a and f + i*dy == b:
                    return 1
        # move in diagonal four directions 
        for direction in [[1,1],[-1,-1],[-1,1],[1,-1]]:
            dx, dy = direction
            for i in range(1,8):
                # if we spot rook just break, because the bishop may be in a blind spot. no need to check further
                if e + i*dx == a and f + i*dy == b:
                    break
                # if we spot bishop , we can capture queen in 1 move
                if e + i*dx == c and f + i*dy == d:
                    return 1
        return 2
        

        for i in range(9):
            s = []
            for j in range(9):
                if a == i and b == j:
                    s.append('R')
                elif c == i and d == j:
                    s.append('B')
                elif e == i and f == j:
                    s.append('Q')
                else:
                    s.append(' ')

        if a == e :
            if c == e and (b < d < f or f < d < b):
                return 2
            return 1

        if b == f:
            if d == f and (a < c < e or e < c < a):
                return 2
            return 1
        
        if e+ f == c +d:
            if a+b == e + f and (e < a < c or c < a < e):
                return 2
            return 1
        
        if e - f == c - d:
            if e-f == a-b and (e < a < c or c < a < e):
                return 2
            return 1
        
        return 2