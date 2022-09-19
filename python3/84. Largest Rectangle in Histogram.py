class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        
        
        
        
        
        
        
        
        
        stack = []

        res = 0

        for i, h in enumerate(heights):

            real_i  = i
            #print(stack)
            while stack and stack[-1][1] > h:
                old_i,old_h = stack.pop()
                print((i - old_i) * old_h)
                res = max(res,  (i - old_i) * old_h)
                real_i = old_i

            stack.append((real_i,h))

        #print(stack)
        for i,h in stack:
            #print( (len(heights) - i) * h)
            res = max(res,  (len(heights) - i) * h)

        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        stack = []
        
        maxArea = 0
        
        for i, h in enumerate(heights):
            start = i
            print(stack)
            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                print(height * ( i - index))
                maxArea = max(maxArea, height * ( i - index))
                start = index

            stack.append((start,h))

        print(stack)
        for index, h in stack:
            print(h * (len(heights) - index))
            maxArea = max(maxArea, h * (len(heights) - index))
            
        
        return maxArea
        
        '''