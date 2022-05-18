class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        
        if num == "10":
            return "0"
        
        prev = 0
        stack = []
        
        


        for c in num:
            
            while len(stack) > 0 and c < stack[-1] and k > 0 :
                stack.pop()
                k -= 1
            
            stack.append(c)
            
        val = "".join(stack[:len(stack)-k])

        return str(int(val)) if val else "0"

    