class Solution:
    def reformat(self, s: str) -> str:
        res = []

        if not s:
            return ''

        d =[]
        n = []
        
        for c in s:
            if c.isdigit():
                d.append(c)
            else:
                n.append(c)

        #dc = sum([c.isdigit() for c in s ])
        #ndc = sum([not c.isdigit() for c in s ])
        
        if abs(len(d)-len(n)) > 1:
            return ''
        
        if len(d) > len(n):
            d, n = n, d
        
        i = 0
        j = 0
        cc = 0
        while cc < len(s):
            if cc%2 == 1:
                res.append(d[i])
                i+=1
            else:
                res.append(n[j])
                j+=1
                
            cc += 1
        return ''.join(res)
        
        '''
        prevD = not s[0].isdigit()

        for c in s:
            if c.isdigit():# and prevD = False:
                if prevD == False:
                    res.append(c)
                    prevD = True
                else:
                    return ''
            else:
                if prevD == True:
                    res.append(c)
                    prevD = False
                else:
                    return ''

        return ''.join(res)
        '''