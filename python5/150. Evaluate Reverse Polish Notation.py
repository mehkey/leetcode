class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def isNumber(n):
            try:
                int(n)
                return True
            except ValueError:
                return False

        def isSpecial(n):
            return n == '+' or n == '-' or n == '*' or n =='/'

        stack = []
        
        for i in range(len(tokens)):
            n = tokens[i]
            
            if isNumber(n):
                stack.append(n)
            else:
                v2 = stack.pop()
                v1 = stack.pop()

                if n == '+':
                    stack.append(str(int(v1) + int(v2)))
                elif n == '-':
                    stack.append(str(int(v1) - int(v2)))
                elif n == '*':
                    stack.append(str(int(v1) * int(v2)))
                elif n == '/':
                    stack.append(str(int(v1) / int(v2)).split(".")[0])

        return int(stack[0])
    
    