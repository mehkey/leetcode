class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:

        nums.sort()

        ps = defaultdict(int)

        for n in nums:
            
            psc = deepcopy(ps)
            
            for k in list(ps.keys()):
                v = ps[k]
                if k + n <= target:
                    psc[k+n] = max(v+1, ps[k+n])
            
            psc[n] = max(psc[n] ,1)
            
            ps = psc
   
        return ps[target] if ps[target] != 0 else -1
