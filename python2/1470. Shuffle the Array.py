class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        res = []
        
        j = n
        for i in range(n):
            res.append(nums[i])
            res.append(nums[j])
            j+=1
        
        return res