class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:

        @lru_cache(None)
        def dfs(pos, slots):
            
            #print(pos, slots)
            maxium = 0
            
            if pos >= len(nums):
                return 0
            
            for i in range(1,numSlots+1):
                #print(i)
                b = (10 ** (i-1))
                cur = slots // b
                #print(slots)
                #print((10 ** (i-1)))
                cur = (cur%10) % 3
                #print(cur)
                
                if cur > 0:
                    #print(cur)
                    #n_slots = slots[0:i-1] + str(cur-1) + slots[i:]
                    n_slots = slots - b
                    #print(n_slots)
                    #print(n_slots)
                    maxium = max(maxium, (nums[pos]&i) + dfs(pos+1, n_slots ) )
            #print(maxium)  
            return maxium

        return dfs(0, int( "1" +  "2"*numSlots  ))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        
        #@lru_cache(None)
        def dp(pos, room):
            if pos == len(nums): return 0

            res = 0
            for slot in range(1, numSlots+1):
                # if slot is 3, then 1 item in it worth 100 = 10 ** 2
                base = 10 ** (slot-1) # value of 1 item of this slot

                # how many spots are available in this slot.
                # if we had room encoded as 1211,
                # and we want to see how much room is available in slot 3:
                # then base = 10 * (slot-1) = 100
                # then left = 1211 // base % 10 = 1211 // 100 %12 = 12 % 10 = 2
                left = room // base % 10
                if left > 0:
                    res = max(res, (nums[pos]&slot) + dp(pos+1, room - base))
            return res

        # initially every slot has room for 2 items. for example:
        # if we have 3 slots we make string '222' converted to int: 222
        return dp(0, int('2'*numSlots))
        """