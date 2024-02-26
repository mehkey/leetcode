class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        
        
        N = len(s)

        arr = [ord(l) - ord('a') for l in s]

        @cache
        def dp(i, extra, bm):
            if i == N:
                return 0

            oldbm = bm

            bm |= (1 << arr[i])

            count = bm.bit_count()

            res = 0

            if count > k:
                res = max(res, dp(i+1, extra,  1 << arr[i]) + 1)
            else:
                res  = max(res, dp(i+1, extra, bm ))

            if extra :
                for j in range(26):
                    nbm = oldbm | (1 << j)
                    count = nbm.bit_count()
                    if count > k:
                        res = max(res, dp(i+1, False, 1 << j) + 1)
                    else:
                        res = max(res, dp(i+1, False, nbm) )
            return res

        return dp(0,True,0) + 1

        '''
        if k == 1:
            return len(s)

        prev = 'X'
        count = 0
        tmp = []

        for c in s:
            if c != prev:
                tmp.append(count)
                count =1
                prev = c
            else:
                count += 1
        tmp.append(count)
        
        tmp = tmp[1:]
            
        #print(tmp)

        @cache
        def dp(i, changed):
        
            if i == N:
                return 0
            
            h = set()
            
            m = 0
                            
            if not changed:
                for j in range(i,N):

                    h.add(s[i])
                    if len(h) == k:
                        m = max(m, dp(j+1, True) + 1)
                        break

            h = set()

            #if changed:
                for j in range(i,N):

                    h.add(s[i])
                    if len(h) == k:
                        m = max(m, dp(j+1, changed) + 1)
                        break

            return m

        return dp(0, False)
        '''