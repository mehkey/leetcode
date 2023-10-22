class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
if len(grid) == 1:
            return [0] if all(num == 0 for num in grid[0]) else []
        d = {}
        for r, row in enumerate(grid):
            num = sum(cell << c for c, cell in enumerate(row))
            for i in range(32):
                if (i & num) == 0 and i in d:
                    return [d[i], r]
            d.setdefault(num, r)    
        return []