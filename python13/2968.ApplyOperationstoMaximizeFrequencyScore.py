class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        N = len(nums)
        pref = [0] + list(accumulate(nums))
        ans = 0
        l = 0
        for r in range(1, N + 1):
            mid = (l + r) // 2
            median = nums[mid]
            cost = abs((r - mid) * median - (pref[r] - pref[mid]))
            cost += abs((mid - l) * median - (pref[mid] - pref[l]))
       
            if cost > k:
                l += 1

            ans = max(ans, r - l)

        return ans

        notValid = lambda l, n: (acc[l] + acc[n-l] - 2*acc[n//2] - 
                                                 nums[n//2]*(n%2) > k)

        nums.sort()
        acc = list(accumulate(nums, initial = 0))
        left = ans = 0

        for rght in range(len(nums)):
            while notValid(left, left+rght+1): left+= 1
            ans = max(ans, rght - left)
           
        return ans+1

        l = 1
        r = len(nums)

        nums.sort()
        #print(nums)
        # 1 2 4 6

        def cal(mid):
            #print(mid)
            #diff = [0] * len(nums)
            tot = 0

            totdiff = 0
            cur = deque()
            for i in range(mid):
                tot += nums[i]
                cur.append(nums[i])
            #cur = []
            
            avg = median(cur)#round(tot / mid)
            
            #totdiff = sum([abs(nums[i]-avg) for i in range(mid)])
            
            totdiff = sum([abs(n-avg) for n in cur])
            
            #print(totdiff, k, avg, mid)
            #print([nums[i] for i in range(mid)], totdiff, k, mid)
            if totdiff <= k:
                return True
            
            for i in range(mid,len(nums)):
                #tot += nums[i]
                #tot -= nums[i-mid]
                cur.append(nums[i])
                cur.popleft()
                
                #print('tot', tot)
                #avg = median([nums[i] for i in range(i-mid+1,i+1)]) #round(tot / mid)
                avg = median(cur) #round(tot / mid)
                
                #avgdiff = newavg - avg
                #print('avgdiff', avgdiff)
                #totdiff -= abs(nums[i-mid-1] - avg)
                #totdiff += abs(nums[i] - avg)
                #otdiff += avgdiff * mid
                
                #avg = newavg
                #totdiff = sum([abs(nums[j]-avg) for j in range(i-mid+1,i+1)])
                totdiff = sum([abs(n-avg) for n in cur])
                #print([nums[i] for i in range(i-mid+1,i+1)], totdiff, k, mid)
                #print(totdiff, k, avg, tot, mid, i)
                if totdiff <= k:
                    return True

            return False
            
            #7 tot, 
            
            '''
            i = 0
            for n in nums:
                diff[i] = abs(n - mid)
                i+=1
            
            diff.sort()
            count = 0
            res = 0
            kk = k
            #print(diff)
            for d in diff:
                if kk - d >= 0:
                    res += 1
                    kk -= d
                else:
                    break
            return res
            '''
        
        ms = 1
        while l <= r:
            #print(l,r)
            mid = (l+r) //2
            
            #print(mid, cal(mid))
            if cal(mid) :
                ms = max(ms, mid)
                l = mid + 1
            else:
                #ms = max(ms, mid)
                r = mid - 1
        
        return ms
        
        '''
        l = 0
        r = max(nums)
        
        nums.sort()
        ma = 0
        diff = [0] * len(nums)
        
        #print(nums)
        def cal(mid):
            #diff = [0] * len(nums)
            i = 0
            for n in nums:
                diff[i] = abs(n - mid)
                i+=1
            
            diff.sort()
            count = 0
            res = 0
            kk = k
            #print(diff)
            for d in diff:
                if kk - d >= 0:
                    res += 1
                    kk -= d
                else:
                    break
            return res
        
        
        while l<=r:
            mid = (l+r) //2
            cl = cal(l)
            cc = cal(mid)
            cr = cal(r)
            ma = max(ma,cc,cl,cr)
            #print(mid,l,r)
            #print('tot', cc, cl,cr)
            #if cl == cr == cc:
            #    return cc
            
            if cc >= cl and cc >= cr:
                cl = mid - mid //2 
                cr = mid + mid //2 
            if cl >= cc and cl >= cr:
                r = mid -1
            elif cr >= cc and cr >= cc:
                l = mid + 1

        
        while l<=r:
            cc = cal(l)
            ma= max(ma,cc)
            l+=1
        

        return ma
        '''
            