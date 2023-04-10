class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1: return -1
        m, n = len(grid), len(grid[0])
        visited = set()
        pq = [(grid[0][0], 0, 0)]

        while pq:
            time, row, col = heappop(pq)
            if row == m-1 and col == n-1: return time
            if (row, col) in visited: continue
            visited.add((row, col))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                    wait = 1 if ((grid[r][c] - time) % 2 == 0) else 0
                    heappush(pq, (max(time + 1, grid[r][c] + wait), r, c))

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        m, n = len(grid), len(grid[0])
        heap = [(0, 0, 0)]
        min_time = [[inf] * n for _ in range(m)]
        min_time[0][0] = 0
        
        while heap:
            curr_time, r, c = heappop(heap)
            for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if 0 <= r + dr < m and 0 <= c + dc < n:
                    if curr_time + 1 >= min_time[r + dr][c + dc]:
                        continue
                    else:
                        if (curr_time + 1 - grid[r + dr][c + dc]) % 2 == 0:
                            min_time[r + dr][c + dc] = max(curr_time + 1, grid[r + dr][c + dc])
                        else:
                            min_time[r + dr][c + dc] = max(curr_time + 1, grid[r + dr][c + dc] + 1)
                        heappush(heap, (min_time[r + dr][c + dc], r + dr, c + dc))
        return min_time[-1][-1]