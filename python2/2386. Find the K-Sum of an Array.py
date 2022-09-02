class Solution:
    def kSum(self, nums: List[int], k: int) -> int:

        total = sum(map(lambda x: 0 if x < 0 else x, nums))

        nums = sorted(list(map(lambda x: -x if x < 0 else x, nums)))
        
        h = [[nums[0],0]]
        
        #print(nums)
        #print(total)
        res = 0
        for j in range(k - 1):

            cur = heappop(h)

            res = cur[0]

            if cur[1] + 1 < len(nums):
                heappush(h, [cur[0] - nums[cur[1]] + nums[cur[1]+1], cur[1]+1])
                heappush(h, [cur[0] + nums[cur[1]+1], cur[1]+1] )

        return total - res

        """
        total = sum(max(0, num) for num in nums)

        pos = sorted([abs(num) for num in nums])
        #print(pos)
        s, heap = 0, [(pos[0], 0)]
        for j in range(k - 1):
            #print(heap)
            s, i = heappop(heap)
            if i + 1 < len(nums):
                heappush(heap, (s - pos[i] + pos[i + 1], i + 1))
                heappush(heap, (s + pos[i + 1], i + 1))

        return total - s
        

        total = sum(max(0, num) for num in nums)

        pos = sorted([abs(num) for num in nums])

        s, heap = 0, [(pos[0], 0)]

        for j in range(k - 1):

            s, i = heappop(heap)
            if i + 1 < len(nums):
                heappush(heap, (s - pos[i] + pos[i + 1], i + 1))
                heappush(heap, (s + pos[i + 1], i + 1))

        return total - s
        
        
        """
