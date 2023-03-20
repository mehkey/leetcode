class Solution:
    def findScore(self, nums: List[int]) -> int:

        h = []

        for i,n in enumerate(nums):
            h.append((n,i))

        heapify(h)
        s = set()

        val = 0

        while h:

            v,i = heappop(h)

            if i in s:
                continue
            else:
                s.add(i)

                if i>0:
                    s.add(i-1)

                if i < len(nums)-1:
                    s.add(i+1)

                val += v

        return val

def findScore(self, A: List[int]) -> int:
        seen = [0] * (len(A) + 1)
        res = 0
        for a,i in sorted([a,i] for i,a in enumerate(A)):
            if seen[i]: continue
            res += a
            seen[i] = seen[i - 1] = seen[i + 1] = 1
        return res