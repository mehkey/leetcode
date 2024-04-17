class Solution:
    def minRemoveToMakeValid(self, ss: str) -> str:
        
        s= []
        res = []
        N = len(ss)
        for i in range(N):
            c = ss[i]
            if c == '(':
                s.append(c)
                res.append(c)
            elif c == ')':
                if s and s[-1] == '(':
                    res.append(c)
                    s.pop()
                else:
                    pass
            else:
                res.append(c)
        
        ss = res
        s = []
        res = []
        N = len(ss)
        for i in range(N-1,-1,-1):
            c = ss[i]
            if c == ')':
                s.append(c)
                res.append(c)
            elif c == '(':
                if s and s[-1] == ')':
                    res.append(c)
                    s.pop()
                else:
                    pass
            else:
                res.append(c)
        return ''.join(res[::-1])
        '''
        def change(ss):
            res = []

            for c in ss:

                if c == '(':
                    s.append(c)
                    res.append(c)
                elif c == ')':
                    if s and s[-1] == '(':
                        res.append(c)
                        s.pop()
                    else:
                        pass
                else:
                    res.append(c)
            return res
        
        rr = change(ss)
        
        for i,c in enumerate(rr):
            if c == '(':
                rr[i] =')'
            elif c == ')':
                rr[i] = '('

        rr = change(rr[::-1])
        
        for i,c in enumerate(rr):
            if c == '(':
                rr[i] =')'
            elif c == ')':
                rr[i] = '(
        '''
        #return rr[::-1]
        #for i in range()