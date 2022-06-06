class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        
        # a a b b b a
        
        # 
        
        
        for c in s:
            
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c,1])
            
            if stack[-1][1] == k:
                stack.pop()
        
        res = ""
        for c, i in stack:
            for j in range(i):
                res += c
        
        return res
            
        """
            stack.append(c)
            
            count = 0
            for j in range(0,k):
                
                if k <= len(stack) and stack[ len(stack) - 1 - j] == c:
                    count += 1
                else:
                    break
            
            #print(count)
            #print(stack)
    
            if count == k :
                for j in range(k):
                    stack.pop()
            
        #print(stack)
        return "".join(stack)
        """
