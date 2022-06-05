class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        
        # a a b b b a
        
        # 
        
        
        for i,c in enumerate(s):
            
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
