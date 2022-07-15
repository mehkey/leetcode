class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int, sum: int, seen: set) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or not grid[i][j] or (i, j) in seen:
                return sum 
            seen.add((i, j))
            sum += grid[i][j]
            mx = 0
            for x, y in ((i, j + 1), (i , j - 1), (i + 1, j), (i - 1, j)):
                mx = max(dfs(x, y, sum, seen), mx)
            seen.discard((i, j))   
            return mx

        m, n = len(grid), len(grid[0])
        return max(dfs(i, j, 0, set()) for j in range(n) for i in range(m))