class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        s = set()

        su = 0
        q = Deque()
        sa = 0
        
        for i, n in enumerate(nums):
            
            if n in s:
                while q and q[0] != n:
                    v = q.popleft()
                    s.remove(v)
                    sa -= v
                if q[0] == n:
                    v =q.popleft()
                    s.remove(v)
                    sa -= v

            sa += n
            s.add(n)
            q.append(n)
            
            if len(q) > k:
                v =q.popleft()
                s.remove(v)
                sa -= v

            if len(s) == k:
                su = max(su , sa)
                
        return su