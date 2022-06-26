class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        #tokens.reverse()
        
        print("-11".isdigit())
        #while len(tokens) > 1:
        
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
            #print(stack)
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
                    #print(int(v1))
                    #print(int(v2))
                    #print(int(v1) / int(v2))
                    #print(math.floor(int(v1) / int(v2)))
                    
                    stack.append(str(int(v1) / int(v2)).split(".")[0])

        return stack[0]
    
    