class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        


        ind = nums.index(k)

        
        N = len(nums)
        
        res = 0

        totG = 0
        totS = 0
        

        count = 1
        
        hm = defaultdict(int)
        hm[0] = 1
        
        for i in range(ind+1,N):
            if nums[i] > k:
                totG += 1
            else:
                totG -= 1
            
            hm[totG] += 1
        
        
        res += hm[0] + hm[1]

        totS = 0
        for i in range(ind-1,-1,-1):
            if nums[i] < k:
                totS += 1
            else:
                totS -= 1
            
            res += hm[totS] + hm[totS+1] 
        
        return res