class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []
        
        for char in num:
            
            while  k > 0 and stack and stack[-1] > char:
                stack.pop()
                k -=1
            
            stack.append(char)
        
        res = "".join(stack[:len(stack)-k])
        
        return str(int(res)) if res else "0"
        
        '''1
        
        1 4
        
        1 3
        
        1 2
        
        1 2 2 
        
        1 1 9
        
        '''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if num == "10":
            return "0"

        prev = 0
        stack = []

        for c in num:
            print(stack)
            while len(stack) > 0 and c < stack[-1] and k > 0 :
                stack.pop()
                k -= 1

            stack.append(c)

        val = "".join(stack[:len(stack)-k])

        return str(int(val)) if val else "0"
