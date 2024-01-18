class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        res = set()
        xx= defaultdict(set)
        yy = defaultdict(set)
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    xx[x].add((x,y))
                    yy[y].add((x,y))

        for x in xx.values():
            if len(x) > 1:
                for v in  x:
                    res.add(v)
        
        for y in yy.values():
            if len(y) > 1:
                for v in y:
                    res.add(v)

        #print(res)
        return len(res)