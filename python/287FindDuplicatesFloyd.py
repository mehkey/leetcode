class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        #total = sum(nums)
        
        #n = len(nums)
        
        #target = int((n - 1) * (n) / 2)
        
        #print(target)
        
        #print( 1 + 2 + 3 + 4)
        
        #return total - target
        
        fast = 0
        slow = 0
        while True:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
            if fast == slow:
                break
        #print(fast)
        slow2 = 0
        while True:
            if slow == slow2:
                break
            slow = nums[slow]
            slow2 = nums[slow2]

        #print(slow)
        return slow2
