class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        """
        
        
        nums = 1 2 3 4 5 6 7 8 9
        
        target = 35
        
        
        Naive Brute Force: 
        
        4 Loops:
            each loop is a new number
            if sum == target
            add to resuslts
            
        O(N ^ 4 )
        
        
        SORT O(n log n)
        
        binary search O(log n)
        
        
        2 LOOPS
            Search for last 2 numbers O(n ^3)

        nums = 1 2 3 4 5 6 7 8 9
        
        2 numbers
        
        1 and 3  -> [4,5,6,7,8,9]
                     L         R
                     
        1,3
        if total < target
              make L larger
        
        if total > target
              make R smaller
        



        -> Clarify
        -> Picture
        -> Approaches (runtime)
        -> Run throuth example
        -> Code
        -> Test example
        -> Edge case/optimization
        
        
        
        
        
        nums.sort()
        
        res = []
        pairs = set()
        
        def s(l,r, newtarget, i, j):
            
            while l < r:
                
                total = nums[l] + nums[r] 
                
                if total == newtarget:
                    res.append([nums[i],nums[j],nums[l],nums[r]])
                    l+= 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                        
                elif total < newtarget:
                    l += 1
                else:
                    r -= 1

        for i in range(0,len(nums)-3):
            for j in range(i+1, len(nums)-2):
                #if nums[i] == nums[j]:
                #    continue
                if i>0 and nums[i] == nums[i-1]:
                    continue
                
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                    
                total = nums[i] + nums[j]
                #if (nums[i],nums[j]) not in pairs:
                    #pairs.add((nums[i],nums[j]))

                s(j+1, len(nums)-1, target - total, i, j )

        return res
        
        
        """
        
        nums.sort()
        
        res = []
        
        current = []

        def kSum(k, start, end, target):
            
        
            if k > 2:

                for i in range(start,len(nums)-k+1):
                    if i>start and nums[i] == nums[i-1]:
                        continue

                    current.append(nums[i])
                    
                    kSum(k-1, i+1, len(nums)-1, target-nums[i])

                    current.pop() # popleft

            elif k == 2:
                
                l = start
                r = end
                
                while l < r:
                
                    total = nums[l] + nums[r] 

                    if total == target:
                        res.append( current + [nums[l],nums[r]])
                        l+= 1
                        while l < r and nums[l] == nums[l-1]:
                            l+=1

                    elif total < target:
                        l += 1
                    else:
                        r -= 1
            else:
                raise Exception("K >= 2") 

        kSum(4,0,len(nums),target)
        
        return res
        
        