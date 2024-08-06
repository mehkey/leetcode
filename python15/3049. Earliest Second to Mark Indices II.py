class Solution:
    def earliestSecondToMarkIndices(self, A: List[int], B: List[int]) -> int:
        firsts = {}
        for i, b in enumerate(B):
            if A[b - 1] and b not in firsts:
                firsts[b] = i
        
        firsts_inv = {i: b for b, i in firsts.items()}

        def possible(bound):
            # Is B[:bound] enough to clear A?
            pq = []
            mark = 0

            for i in range(bound - 1, -1, -1):
                if i in firsts_inv:
                    heappush(pq, A[firsts_inv[i] - 1])
                    
                    if mark:
                        mark -= 1
                    else:
                        mark += 1
                        heappop(pq)
                else:
                    mark += 1

            return sum(A) - sum(pq) + len(A) - len(pq) <= mark

        lo, hi = 0, len(B) + 1
        while lo < hi:
            mi = lo + hi >> 1
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        
        return lo if lo <= len(B) else -1
        

        
        N = len(nums)
        M = len(ci)
        
        l = N -1
        r = M -1
        res = inf
        
        s = sum(nums)

        if s + len(nums) > len(ci) :
            return -1

        def test(k):
            nums1 = nums[:]

            count = 0
            need = 0
            
            for j in range(k, -1, -1):
                i = ci[j] - 1
                if nums1[i] == -1:
                    if need:
                        need -= 1
                else:
                    need += nums1[i]
                    nums1[i] = -1
                    count += 1
            
            if need == 0 and count == len(nums1):
                return True
            
            return False

        while l <= r:
            
            mid = (l+r) // 2

            if test(mid):
                res = min(res, mid)
                r = mid -1

            else:
                l = mid + 1
        
        return -1 if res == inf else res + 1