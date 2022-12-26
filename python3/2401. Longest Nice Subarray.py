class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        l = 0
        q = deque()
        cur = 0

        for i in nums:

            while q and (i & cur) :
                cur ^= q[0]
                q.popleft()
                
            
            cur = cur | i
            q.append(i)

            l = max(l, len(q))

        return l

