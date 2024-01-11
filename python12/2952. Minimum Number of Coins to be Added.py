class Solution:
    def minimumAddedCoins(self, nums: List[int], target: int) -> int:

        '''
        #for i in range(coins):
        ss = sum(coins)

        sss = set(coins)

        res = 0
        
        m = min(coins)
        
        for i in range(1,target-ss+1):
            
            res += i - ss
        
        for i in range(1,min(m+1,target)):
            res += i
        '''

        nums.sort()

        current_max = 0
        additions = 0
        index = 0

        while current_max < target:
            #print(index, current_max)
            if index < len(nums) and nums[index] <= current_max + 1:
                current_max += nums[index]
                index += 1
            else:
                current_max += current_max + 1
                additions += 1

        return additions

