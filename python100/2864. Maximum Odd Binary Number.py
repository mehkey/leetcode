class Solution:

    def maximumOddBinaryNumber(self, s: str) -> str:

        '''
        m = 0

        #bits = bin(s)[2:]

        #return 0
        
        for b in s:
            print(b)
        
        for c in s:
        
        return 0
        
        '''
        m = 0
        
        ss = len(s)
        tt = s.count("1")
        
        res = [i for i in s]
        
        '''
        if res[-1] == '1':
            return s
        
        else:
            first = len(res)-1
            while first >= 0:
                first -= 1
                if res[first] == '1':
                    break
            res[first] = '0'
            res[-1] = '1'
            return ''.join(res)
        '''
        #res = bin(m)[2:]

        res = '1'*(tt-1) + (len(res)-tt)*'0' + '1'
        
        return res
        
        #for i in range(1<<ss):

        #if i.bit_count() == tt and i % 2 == 1:
            #m = max(m, i)

        res = bin(m)[2:]

        res = (ss - len(res))*'0' + res
        return res
