class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        idx = 0
        for i in range(1, n + 1):
            if n % i == 0:
                idx += 1
            if idx == k:
                return i
        return -1