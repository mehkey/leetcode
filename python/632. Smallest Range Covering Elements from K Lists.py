class Solution:
    def smallestRange(self, A: List[List[int]]) -> List[int]:
        pq = [(row[0], i, 0) for i, row in enumerate(A)]
        heapq.heapify(pq)

        ans = -1e9, 1e9
        print(pq)
        right = max(row[0] for row in A)
        print(right)
        while pq:
            left, i, j = heapq.heappop(pq)
            print(left)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j + 1 == len(A[i]):
                return ans
            v = A[i][j+1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j+1))