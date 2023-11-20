class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:

        n = len(grid)

        hm = defaultdict(bool)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                if grid[i][j] == 1:
                    hm[j] = True

        for i in range(n):
            if hm[i] == False:
                return i
