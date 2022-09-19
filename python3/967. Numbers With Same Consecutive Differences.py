class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:

        '''
        def valid(n):
            
            s = str(n)
            
            for i in range(len(s)-1):
                c1 = s[i]
                c2 = s[i+1]
                if abs(ord(c1) - ord(c2)) != k :
                    return False

            return True
            
        res = []
        for i in range(10**(n-1), 10**(n )) :
            if valid(i):
                res.append(i)
                
        return res
        '''
        cur = range(1, 10)
        for i in range(N - 1):
            #print(cur)
            cur = [x * 10 + y for x in cur for y in [x%10+K,x%10-K] if 0 <= y <= 9]
            #cur = {x * 10 + y for x in cur for y in [x % 10 + K, x % 10 - K] if 0 <= y <= 9}
        #print(cur)
        return sorted(set(cur))
            
            