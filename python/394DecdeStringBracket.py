class Solution:
    def decodeString(self, s: str) -> str:
        
        
        """
        
        3[a]2[bc]
        
        | 2 |  [ | b |c | | | | 
        
        
        k 2
        e bc
        
        res = aaabcbc
        
        """
        
        stack = []
        
        #res = ""
        
        for c in s:
            
            #print(c)
            #print(stack)
            if c == ']':
                
                e = ""
                
                while stack[-1] != '[':
                    e = stack.pop() + e
                
                stack.pop() #remove [ opening bracket
                
                kString = ""
                while stack and stack[-1].isdigit():
                    kString =  stack.pop() + kString
                
                for i in range(int(kString)):
                    stack.append( e )

            else:
                stack.append(c)
        
        return "".join(stack)