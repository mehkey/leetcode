class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        N = len(colsum)
        res = [[0]*N for _ in range(2)]

        i = 0

        for n in colsum:
            #print(upper,lower)
            if n > 2 or n < 0:
                return []
            if n == 2:
                res[0][i] = 1
                res[1][i] = 1
                upper -= 1
                lower -= 1
            i+=1
        if upper < 0 or lower < 0:
            return []
        i=0
        for n in colsum:
            if n == 1:
                if upper > 0:
                    res[0][i] = 1
                    upper -=1
                elif lower > 0:
                    res[1][i] = 1
                    lower -= 1
                else:
                    return []

            i+=1

        if upper > 0 or lower > 0:
            return []
        
        return res
        