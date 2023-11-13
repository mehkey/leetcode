class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        A = maxHeights
        n = len(A)
        def f(A):
            res = [0] * n
            stack = [-1]
            for i in range(n):
                while len(stack) > 1 and A[stack[-1]] > A[i]:
                    stack.pop()
                res[i] = res[stack[-1]] + (i - stack[-1]) * A[i]
                
                stack.append(i)
                #print(stack)
                #print(res)
            return res
        print(A)
        print(A[::-1])
        print(f(A), f(A[::-1]))
        return max(pre + suf - a for pre,suf,a in zip(f(A), f(A[::-1])[::-1], A))


        l = 0
        mm = len(maxHeights)
        
        mmm = 0
        
        s = [0] * len(maxHeights)
        sa = [0] * len(maxHeights)
        
        l = [0]* len(maxHeights)
        
        sl = [0] * len(maxHeights)
        
        cur = float('inf')
        for i in range( mm ):
            cur = min(cur,maxHeights[i])
            s[i] = cur
        
        cur = float('inf')
        for i in range( mm -1, -1, -1):
            cur = min(cur,maxHeights[i])
            l[i] = cur

        sa = list(accumulate(s,operator.add))
        sl = list(accumulate(l,operator.add))
        for start in range( mm ):
            tot= sl[start-1] if start-1 >= 0 else 0 + maxHeights[start] + sa[start+1] if start+1 < mm else 0
            mmm = max(mmm, tot)

        return mmm

        #print(s)
        #print(l)
        '''
        for start in range( mm ):

            l = start -1
            r = start +1
            
            tot = maxHeights[start]
            cur = tot
            while l >= 0 :
                
                cur = min(cur,maxHeights[l])
                tot += cur
                l-= 1
            cur = tot
            while r <= len(maxHeights) -1:
                cur = min(cur,maxHeights[r])
                tot += cur
                r+= 1
            
            mmm = max(mmm, tot)
        return mmm
        '''