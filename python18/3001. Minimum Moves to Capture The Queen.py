class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:

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
            #print(s)

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