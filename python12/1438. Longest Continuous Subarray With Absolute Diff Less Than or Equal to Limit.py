class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        maxd = collections.deque()
        mind = collections.deque()
        i = 0
        for a in nums:
            print(maxd, mind)
            while len(maxd) and a > maxd[-1]: maxd.pop()
            while len(mind) and a < mind[-1]: mind.pop()
            maxd.append(a)
            mind.append(a)
            print(maxd, mind)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[i]: maxd.popleft()
                if mind[0] == nums[i]: mind.popleft()
                i += 1
                print(i)
        return len(nums) - i

        n = len(nums)

        mi = inf
        ma = -inf
        
        ma = []
        mi = []

        l = 0
        
        ml,mr = -1,-1
        for r in range(n):
            
            heappush(mi, (nums[r],r))
            heappush(ma, (-nums[r],r))
            
            while l < n and (-ma[0][0] - mi[0][0]) > limit:
                
                l+=1

                while ma and ma[0][1] < l:
                    heappop(ma)
                while mi and mi[0][1] < l:
                    heappop(mi)
            
            if ml == -1 or r - l > mr - ml:
                ml = l
                mr = r

        return mr - ml +1

            
            
            