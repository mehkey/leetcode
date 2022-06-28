class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        """
        
        HashMap and add and remove...
        
        O( n * k ) easy bruteforce...
        
        HashMap
        
        
        1 3 -1
        
        HSet
        
        (1,3,-1)
        
        remove
        
        1
        
        add 
        
        -3
        
        (3,-1,-3)
        
        queue 3 -1 -3
        
        -6
        
        """
        
        output = []
        
        q = collections.deque() #index
        
        l = 0
        
        r = 0
        
        while r < len(nums):
        
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)
            
            if q and l > q[0]:
                q.popleft()
            
            if r - l  == k -1:
                output.append(nums[q[0]])
                l+= 1
                
            r += 1
            
        return output