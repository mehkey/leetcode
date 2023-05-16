from sortedcontainers import SortedSet

class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        

        pos = {a: i for i, a in enumerate(A)}
        res = n = len(A)
        A.sort()
        for i in range(1, n):
            if pos[A[i]] < pos[A[i - 1]]:
                res += n - i
        return res

        '''
        m = min(nums)
        
        #for i,n in enumerate(nums):
        #    nums[i] -= m

        print(nums)

        cc = nums[::]
        
        i = 0

        while i < len(nums)-1:
            cc[i]-=cc[i+1]
            i+=1
        cc[len(nums)-1] -= cc[0] 
        print(cc)
        
        return i

        #for c in nums:
        #    c += nums[i]
                
        
        #for c in nums:
        #    c -= nums[i]

        return 0
        
        
        #for i in range(n):
        
        def countingSort(array, place):
            size = len(array)
            output = [0] * size
            count = [0] * 10

            # Calculate count of elements
            for i in range(0, size):
                index = array[i] // place
                count[index % 10] += 1

            # Calculate cumulative count
            for i in range(1, 10):
                count[i] += count[i - 1]

            # Place the elements in sorted order
            i = size - 1
            while i >= 0:
                index = array[i] // place
                output[count[index % 10] - 1] = array[i]
                count[index % 10] -= 1
                i -= 1

            for i in range(0, size):
                array[i] = output[i]


        # Main function to implement radix sort
        def radixSort(array):
            # Get maximum element
            max_element = max(array)

            # Apply counting sort to sort elements based on place value.
            place = 1
            while max_element // place > 0:
                countingSort(array, place)
                place *= 10

        #v = [1,5,4,6,7,-1,-2]
        
        v = nums
        
        pv = []
        nv = []
        
        for vv in v:
            if vv >= 0:
                pv.append(vv)
            else:
                nv.append(-vv)

        if pv:
            radixSort(pv)
        
        if nv:
            radixSort(nv)

        for i,vv in enumerate(nv):
            nv[i] = -vv

        nv.reverse()
        
        #print(pv)
        #print(nv)
        d = deque(nums)

        qq = deque(nv + pv)

        #h = [*nums]
        
        #heapify(h)
        
        c = 0
        #print(qq)
        #return c
    
        while d:
            
            #if d[0] == h[0]:
            if d[0] == qq[0]:
                d.popleft()
                qq.popleft()
            else:
                d.append(d.popleft())
            c += 1

        return c
        
        #print(v)
        
        return 0
        
#data = [121, 432, 564, 23, 1, 45, 788]
#radixSort(data)
        
        '''

        d = deque(nums[::])
        s = SortedSet(nums, key=lambda x: -x)
        
        c = 0
        
        #print(s)
        #print(s[-1])
        #s.pop()
        #print(s)
        #print(s[-1])
        #print(s)

        while d:
            #print(d)
            #print(s)
            if d[0] == s[-1]:
                d.popleft()
                s.pop()
            else:
                d.append(d.popleft())

            c += 1
        
        return c

        
        d = deque(nums)

        qq = deque(sorted(nums))

        #h = [*nums]
        
        #heapify(h)
        
        c = 0

        while d:
            
            #if d[0] == h[0]:
            if d[0] == qq[0]:
                d.popleft()
                qq.popleft()
            else:
                d.append(d.popleft())
            c += 1

        return c
        
        