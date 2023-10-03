class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        
        c = 0
        for i in range(0,len(nums)):
            
            for j in range(i+1, len(nums)):
                
                s1 = str(nums[i])[0]
                s2 = str(nums[j])[-1]
                if gcd(int(s1),int(s2)) == 1:
                    c+=1
        
        return c