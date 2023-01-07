class Solution:
    def maximumTastiness(self, prices: List[int], k: int) -> int:
        
        '''
        s = list(set(price))
        s = sorted(s)

        diff = [abs(s[i] - s[j]) for i in range(0,len(s)-1) for j in range(i+1, len(s))]

        diff = sorted(diff)

        return 0

        

        prices.sort()

        l = 0
        r = max(price)
        
        ma = 0
        
        while l <= r:

            m = (l+r) // 2

            for p in prices:

        return 

        '''

        prices.sort()

        def check(val):
            last, count, index = prices[0], 1, 1
            while index < len(prices) and count < k:
                if prices[index] - last >= val:
                    count+=1
                    last = prices[index]
                index+=1
            
            return count >=k

        l,r = 0, prices[-1]

        maxi = 0

        while l<=r:
            m = (l+r)//2
            if check(m):
                maxi = max(maxi,m)
                l = m + 1
            else:
                r = m - 1

        return maxi

        '''
        price.sort()
        #print(price)
        def check(x):
            last, count, i = price[0], 1, 1
            while count < k and i < len(price):
                if price[i] - last >= x:
                    last, count = price[i], count + 1
                i += 1
            return count == k
        lo, hi = 0, max(price)
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1
        '''