class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        
        
        
        
        
        
        '''

        [1,2,3,2]
        [1, 3, 6, 8]

        1,0 

        1,0 2,0

        1,0 2,0 3,0

        1,0 2,0 2,0

        
        '''
        prefix = [0] + list(accumulate(nums))

        s = []

        res = float("-inf")
        #print(prefix)
        for i,n in enumerate(nums):
            #print(s)
            newi = i
            while s and s[-1][0] > n:
                old_n, old_i = s.pop()
                total = (prefix[i] - prefix[old_i]) * old_n
                #print(total)
                res = max(res, total)
                newi = old_i
            s.append((n,newi))
            #print(s)

        for n,i in s:
            total = (prefix[-1] - prefix[i]) * n
            #print(total)
            res = max(res, total)

        return res % ( 10 ** 9 + 7)
        
        
        
        
        
        
        """
         3 2 5
        
         Increasing
         
         1 2 3  HAPPY
         
         1 2 3 2 1. SAD STOP
         
         
         REMOVE FROM ARRAY
         
         
         STACK 
         [pos id, value]
         
         1 2 3 2
         
         [0,1] [1,2] [2,2]         
         
         8 * 1 = 8
         7 * 2 = 14
         5 * 2 = 10
         
         res 14

        time: O(n)
        space: O(n)
         
        """
        
        stack = []
        
        res = float("-inf")
        
        prev = [0]
        
        for n in nums:
            prev.append(prev[-1] + n)
            
        print(prev)
        for i, n in enumerate(nums):
            newi = i
            while stack and len(stack) > 0 and stack[-1][1] > n:
                ip, np = stack.pop()
                total = np * ( prev[i] - prev[ip]) #revisit
                print(total)
                res = max(res, total)
                newi = ip

            stack.append([newi,n])
            print(stack)
        
        for i,n in stack:
            
            total = prev[-1] - prev[i] 
            #print(prev[-1] - prev[i])
            #print(res)
            print(total* n)
            #print(int(total) * n)
            res = max(res,total * n)
                
        return res % ( 10 ** 9 + 7)

        
        
        
        