class Solution:
    def isValid(self, s: str) -> bool:
        
        openings = ['(','{','[']
        parenthesisMap = { ")":"(","]":"[","}":"{"}

        stack = []
        
        for char in s:
            
            if char in openings:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                lastBracket = stack.pop()
                
                if parenthesisMap.get(char) != lastBracket:
                    return False
        

        if len(stack) != 0:
            return False
        
        return True