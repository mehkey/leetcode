class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:

        red = sorted(list(set(nums)))

        hm2 = {}

        for i,v in enumerate(red):
            hm2[v] = i

        hm = defaultdict(int)

        for i,n in enumerate(nums):
            hm[n]+=1

        count = 0
        for i in range(len(nums)):
            n = nums[i]

            ind = hm2[n]

            for j in range(ind+1, len(red)):
                if hm[red[j]] != 0:
                    count+=1
                    hm[red[j]] -=1
                    break

        return count
