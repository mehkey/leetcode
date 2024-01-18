class Solution:
    def findMaximumLength(self, A: List[int]) -> int:

        n = len(A)
        last = [0] + [inf] * n
        acc = [0]
        dp = [0] + [0] * n
        for j in range(n):
            a = A[j]
            acc.append(a + acc[-1])
            i = j
            while last[i] > acc[-1] - acc[i]:
                i -= 1
            last[j + 1] = acc[-1] - acc[i]
            dp[j + 1] = dp[i] + 1

            print(dp)
            print('acc',acc)
            print('last',last)

        return dp[-1]

        '''
        n = len(nums)
        acc = list(accumulate(nums, initial=0))
        
        dp = [0] * (n + 1)
        last_sum = [0] * (n + 1)
        
        dq = deque()
        start = 0
        for i in range(n):
            while dq and acc[i+1] >= last_sum[dq[0]] + acc[dq[0]]:
                start = dq.popleft()
            last_sum[i+1] = acc[i+1] - acc[start]
            dp[i+1] = dp[start] + 1
            while dq and last_sum[dq[-1]] + acc[dq[-1]] > last_sum[i+1] + acc[i+1]:
                dq.pop()
            dq.append(i + 1)
        return dp[-1]

        
        n= len(nums)
        
        prev = inf
        
        streak = 0
        streakCount = 0

        rem = 0
        
        #print(nums)
        
        pa = deque()
        #pac = []
        
        for i in range(n-1,-1,-1):
            v = nums[i]
            #good
            if v < prev:
                
                streak += 1
                streakCount += v

                prev = v
                pa.append(v)
                #pac.append( (pac[-1] if pac else 0) + v)
                #print(pa)
            #bad
            else:
                cur = v
                #print('bad', v, prev, pa)
                if pa and len(pa) > 1 and pa[-1] + cur < pa[-2] and pa[-1] + cur >  pa[-2] + pa[-1]: #and cur + pa[-1] > pa[-1]+ pa[-2]  :
                    pa.append(pa.pop()+pa.pop())

                    pa.append(v)
                    rem += 1
                    continue

                cur = v
                #print('bad', v, prev, ' adding ', (streak) )

                #print('bad', v, prev, pa)

                while pa :
                    cur += pa.pop()
                    rem += 1
                    #print(' adding ', 1)
                    if pa and cur < pa[-1]:
                        break

                pa.append(cur)
                #rem += streak
                #prev = streakCount

                
                #streak = 1
                #streakCount += v
                
                #prev = streakCount
                prev = cur

                #print('now', (streak) , 'prev', )

        return n - rem
        '''