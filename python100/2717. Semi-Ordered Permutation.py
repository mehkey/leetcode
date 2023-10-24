class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        
        count = 0
        
        '''
        #for i in range(len(nums)):
            
        if nums[i] == i+1:
            continue
        else:

            c = nums.index(i+1)

            nums[i], nums[c] = nums[c], nums[i]

            count +=1
        '''
            
        if nums[0] == 1:
            pass
        else:
            c = nums.index(1)

            l = 0
            r = c
            while l < r:
                nums[r], nums[r-1] = nums[r-1], nums[r]
                r-=1
                count += 1
            #nums[0], nums[c] = nums[c], nums[0]

            
            
        n = len(nums)-1
        
        if nums[n] == n+1:
            pass
        else:
            c = nums.index(n+1)

            #nums[n], nums[c] = nums[c], nums[n]

            l = c
            r = n
            while l < r:
                nums[l], nums[l+1] = nums[l+1], nums[l]
                l+=1
                count += 1
                
        return count
