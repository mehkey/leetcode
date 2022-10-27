class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        left = 0
        last_min_k_index = -1
        last_max_k_index = -1
        fixed_bounds_subarrays = 0

        for right, v in enumerate(nums):
            if v < minK or v > maxK:
                left = right + 1
            else:
                if v == minK:
                    last_min_k_index = right
                if v == maxK:
                    last_max_k_index = right
                if last_min_k_index >= left and last_max_k_index >= left:
                    if last_min_k_index < last_max_k_index:
                        fixed_bounds_subarrays += last_min_k_index - left + 1
                    else:
                        fixed_bounds_subarrays += last_max_k_index - left + 1

        return fixed_bounds_subarrays

        '''
        #L = min(nums)
        #R = max(nums)
        
        
        L = minK
        R = maxK
        
        def countSubarrys(n):
 
            return n * (n + 1) // 2
            
        c = defaultdict(int)


        #prevSum = defaultdict(lambda : 0)
        
        
        l = 0
        
        tot = 0
        res = 0
        
        d = Deque()
        
        a = nums

        for i in range(len(nums)):

            
            if a[i] == L or a[i] == R:
                sL = i
            
            if a[i]

            c[a[i]] += 1
            
            
            
            if a[i] > R or a[i] < L:
                #if res >= 0:
                if L != R:
                    #print('add', countSubarrys(c[L]*c[R]))
                    tot += countSubarrys(max(c[L],c[R]))
                else:
                    #print('addddd', countSubarrys(c[L]))
                    tot += countSubarrys(c[L])
                
                #print('addd', res)
                tot += res
                
                res = 0
                c = defaultdict(int)

            if  c[L] > 0 and c[R] > 0 and a[i] > L and a[i] < R:
                res += 1
                
            if  c[L] == 0 and c[R] == 0 and a[i] > L and a[i] < R:
                res += 1
        
        if c[L] > 0 and c[R] > 0:
            if L != R:
                tot += countSubarrys(max(c[L],c[R]))
            else:
                tot += countSubarrys(c[L])
            tot += res

        return tot
        
        
        L = minK
        R = maxK
        
        def countSubarrys(n):
 
            return n * (n + 1) // 2
            
        c = defaultdict(int)


        #prevSum = defaultdict(lambda : 0)
        
        
        l = 0
        
        tot = 0
        res = 0
        
        d = Deque()
        
        a = nums

        for i in range(len(nums)):

            c[a[i]] += 1
            
            
            if a[i] > R or a[i] < L:
                #if res >= 0:
                if L != R:
                    #print('add', countSubarrys(c[L]*c[R]))
                    tot += countSubarrys(max(c[L],c[R]))
                else:
                    #print('addddd', countSubarrys(c[L]))
                    tot += countSubarrys(c[L])
                
                #print('addd', res)
                tot += res
                
                res = 0
                c = defaultdict(int)

            if  c[L] > 0 and c[R] > 0 and a[i] > L and a[i] < R:
                res += 1
                
            if  c[L] == 0 and c[R] == 0 and a[i] > L and a[i] < R:
                res += 1
        
        if c[L] > 0 and c[R] > 0:
            if L != R:
                tot += countSubarrys(max(c[L],c[R]))
            else:
                tot += countSubarrys(c[L])
            tot += res

        return tot
    
    
        
    
        number_servers = len(processingPower)

        left = 0

        max_culsters = 0

        sum_processors = 0

        number_processors = 0

        queue = deque()
         #print("right", right)

            while queue and queue[-1][0] < bootingPower[right]:
                queue.pop()

            queue.append((bootingPower[right],right))
            #print("queue", queue)
            sum_processors += processingPower[right]
            number_processors += 1

            while True:
                if left > right:
                    break

                processing_power = self.calcualte_processing_power(queue[0][0],sum_processors,number_processors)

                if processing_power <= powerMax:
                    max_culsters = max(max_culsters,number_processors)
                    break
                else:
                    sum_processors -= processingPower[left]
                    number_processors -= 1
                    left += 1
                    if queue and left> queue[0][1]:
                        queue.popleft()

        return max_culsters
    
        
        ans=0
		prefsum=0
		d={0:1}
        
        c = defaultdict(int)

		for num in nums:
			prefsum = prefsum + num

			if prefsum-k in d:
				ans = ans + d[prefsum-k]

			if prefsum not in d:
				d[prefsum] = 1
			else:
				d[prefsum] = d[prefsum]+1

		return ans
    
        
        
        def countSubarrys(n):
 
            return n * (n + 1) // 2
 

        def countSubarrays(a,n,L,R):

            res = 0


            exc = 0
            inc = 0
            
            c = defaultdict(int)
            
            prevSum = defaultdict(lambda : 0)

            for i in range(n):

                c[a[i]] += 1
                
                if c[L] >= 1 and c[R] >= 1 and max(c) == :
                    
                    res += 1
                

                if (currsum - Sum) in prevSum:
                    res += prevSum[currsum - Sum]
                
                prevSum[currsum] += 1
                
            return res
                if c[L] >= 1 and c[R] >= 1:
                    
                    res += 1
                    
                
                if (a[i] == R):
                    
                    c[R] += 1
                

                    res = res + (countSubarrys(inc) - countSubarrys(exc))
                    inc = 0
                    exc = 0


                elif (a[i] < L):
                    exc=exc + 1
                    inc=inc + 1


                else:

                    res =res - countSubarrys(exc)
                    exc = 0
                    inc=inc + 1

            res =res + (countSubarrys(inc) - countSubarrys(exc))

            return res
            '''
        
        #mi = min(nums)
        #ma = max(nums)
        
        
        #print(countSubarrays(nums, len(nums), mi, ma))

            
            
        
        