class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        stack = []
        
        def sub2(openN, closeN):
            if openN == closeN and closeN == n:
                res.append("".join(stack))
            
            if( openN > closeN):
                stack.append(")");
                sub2(openN , closeN +1 );
                stack.pop();

            if(openN < n):
                stack.append("(");
                sub2(openN +1 , closeN );
                stack.pop();

        def sub(result, nOpen) -> List[str]:

            if len(result) == n * 2 and nOpen == 0:
                return [result]

            if(len(result) > n*2):
                return []

            if(len(result) > n and nOpen > n):
                return []

            res = []

            res.extend(sub(result+"(", nOpen +1))

            if(nOpen > 0):
                res.extend(sub(result+")", nOpen -1))

            return res
        
        def sub3(result, nOpen,nClose) -> List[str]:

            if nOpen == n and nClose == n:
                return [result]

            res = []

            if( nOpen > nClose):
                res.extend(sub3(result+")", nOpen , nClose+1 ))

            if(nOpen < n):
                res.extend(sub3(result+"(", nOpen +1, nClose))

            return res

        #return sub("", 0,0);
        sub2(0,0)
        return res
        #return sub3("", 0,0);
