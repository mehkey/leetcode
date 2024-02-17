class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        hm = defaultdict(int)
        N = len(nums)
        
        val = -inf
        
        bet = 0
        
        acc = [0] + list(accumulate(nums))

        for i,r in enumerate(nums):

            tar = r - k
            if tar in hm :
                val = max( val , acc[i+1] - acc[hm[tar] ]  )
            tar = r + k
            if tar in hm :
                val = max( val , acc[i+1] - acc[hm[tar] ]  )
            
            if r in hm:
                hm[r] = i # if  acc[i] - acc[hm[r]] < 0 else hm[r]
            else:
                hm[r] = i

        
        return val if val != -inf else 0