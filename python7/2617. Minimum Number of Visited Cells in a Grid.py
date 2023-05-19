
from sortedcontainers import SortedList
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        s0 = [SortedList(range(n)) for _ in range(m)]
        s1 = [SortedList(range(m)) for _ in range(n)]
        q = deque([(0, 0, 1)])

        while q:
            i, j, d = q.popleft()
            if (i, j) == (m-1, n-1):
                return d
            for k in list(s0[i].irange(j+1, min(j+1+grid[i][j], n) - 1)):
                q.append((i, k, d+1))
                s0[i].remove(k)
                s1[k].remove(i)
            for k in list(s1[j].irange(i+1, min(i+1+grid[i][j], m) - 1)):
                q.append((k, j, d+1))
                s1[j].remove(k)
                s0[k].remove(j)
        return -1
    
    
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        
        M = len(grid)
        N = len(grid[0])
        
        ans = [[-1] for i in range(N)] for i in range(M)]
        
        ans2 = [[-1] for i in range(N)] for i in range(M)]
        
        
        ans[0][0] = 0
        
        
        for j in range(1,N):
            if grid[0][j-1] + 1
            ans[0][j] = ans[0][j-1]
            ans2[0][j] = max(ans[0][j], ans[0][j-1])

        for i in range(1,M):
            ans[i][0] = ans[i-1][0]

        for i in range(1,M):
            for j in range(1,N):
                ans[i][j] = min(ans[i][j-1],ans[i-1][j] )
                
                
        return ans[M-1][N-1] 

class FT:
    def __init__(self, size):
        self.SIZE = size
        self.arr = {}

    def put(self, num):
        num += 1
        while num <= self.SIZE:
            self.arr[num] = self.arr.get(num, 0) + 1
            num += num & (-num)

    def get(self, num):
        num += 1
        ret = 0
        while num > 0:
            ret += self.arr.get(num, 0)
            num -= num & (-num)
        return ret

    def remove(self, num):
        num += 1
        while num <= self.SIZE:
            self.arr[num] = self.arr.get(num, 0) - 1
            num += num & (-num)


class Solution:
    def count_fancy_pairs(self, pairs, k1, k2):
        ft = FT(2*(10**5)+1)
        pairs.sort(key=lambda pair: pair[0])
        n = len(pairs)
        for _, y in pairs:
            ft.put(y)
        l, r = 0, n-1
        ans = 0
        while l < r:
            ft.remove(pairs[l][1])
            while r > l and pairs[l][0] + pairs[r][0] > k1:
                ft.remove(pairs[r][1])
                r -= 1
            ans += ft.get(k2-pairs[l][1])
            l+=1
        return ans