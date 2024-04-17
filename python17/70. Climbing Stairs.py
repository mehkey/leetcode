class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        prev_prev = 1
        prev = 2
        for i in range(n-2):
            result = prev_prev + prev
            prev_prev = prev
            prev = result
        return result