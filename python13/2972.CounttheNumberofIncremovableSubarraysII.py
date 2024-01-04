class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        N = len(nums)
        right = []
        left = []
        
        cur = nums[0]
        left.append(nums[0])
        for i in range(1,N):
            if nums[i] > cur:
                left.append(nums[i])
            else:
                break
            cur = nums[i]
        cur = nums[-1]
        right.append(nums[-1])
        for i in range(N-2,-1,-1):
            if nums[i] < cur:
                right.append(nums[i])
            else:
                break
            cur = nums[i]
        right = right[::-1]
        #print(left,right)
        
        if len(right) == N:
            return N * (N+1)//2
        res = len(right)+1
        for i,v in enumerate(left):
            lv = bisect_left(right, v+1)
            
            res += len(right) - lv + 1
        #print(res)
        return res
        '''
        for i in range(1,N):
            if nums[i] <= nums[i-1]:
                fl[i] = True
        
        #print(fl)
        
        res = 0
        lf = 0
        for r in range(N):
            #if not fl[r]:
                #i = r
                #while i >
                #res += N - r
            #else:
                #res += 1
            if fl[r]:   
                #res += factorial(r - lf )
                lf = r
                
            else:
                res += lf
                res += N - r
        #res += factorial(r - lf)
        return res
        
        l = 0
        r =0
        res = 0
        N = len(nums)
        #for r in range(len(nums)):
        for i in range(N):
            for j in range(i,N):
                #sub = nums[i:j]
                
                arr = nums[0:i] + nums[j+1:]
                
                f = False
                for k in range(1,len(arr)):
                    if arr[k] <= arr[k-1]:
                        f = True
                        break
                if not f:
                    #print(arr)
                    res +=1
        return res
        
        '''