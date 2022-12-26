class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        
        '''
        LIS = len(nums) * [1]
        #print(LIS)
        for i in range(len(nums)-2,-1,-1):
            
            curLongest = 1

            for j in range(i+1,len(nums)):

                if(nums[i] < nums[j] and abs(nums[i] - nums[j]) <= k ):
                    curLongest = max(1+LIS[j],curLongest )
               
            LIS[i] = curLongest
        
        
        return max(LIS)
        

        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size
        
        
        sub = [float('inf'), float('inf')]
        for n in nums:
            if n <= sub[0]:
                sub[0] = n
            elif n <= sub[1]:
                sub[1] = n
            else:
                return True
        return False
        
        
        
        def binarySearch(sub, val):
            lo, hi = 0, len(sub)-1
            while(lo <= hi):
                mid = lo + (hi - lo)//2
                if sub[mid] < val:
                    lo = mid + 1
                elif val < sub[mid]:
                    hi = mid - 1
                else:
                    return mid
            return lo
        
        sub = []
        for val in nums:
            pos = binarySearch(sub, val)
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
        return len(sub)
        
        
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and abs(nums[i] - nums[j]) <= k :
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)
        '''
        
        dp_tracker = defaultdict(list)
        n = len(nums)
        dp = [1]*n
        max_till_now = 1
        for i in range(n):
            temp_ans = 1
            max_ans = 0
            
            for j in range(max_till_now, 0, -1):
                ind = bisect_left(dp_tracker[j], nums[i])
                if ind != 0:
                    if k >= (nums[i] - dp_tracker[j][ind-1]) > 0:
                        max_ans = j
                        break
                
            dp[i] = temp_ans + max_ans
            bisect.insort(dp_tracker[dp[i]], nums[i])
            
            max_till_now = max(max_till_now, dp[i])
            
        return max(dp)
        
        #or segment tree