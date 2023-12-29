class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        c = Counter( sum(grid,[]))
        res = [0,0]
        print(c)
        for i in range(1,len(grid)**2+1):
            if i not in c:
                res[1] = i
            elif c[i] > 1:
                res[0] = i
        
        return res