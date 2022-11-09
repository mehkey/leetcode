class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:

        '''
        res = []

        heap1 = [[v,i] for i,v in enumerate(nums)]
        heap2 = [[v,i] for i,v in enumerate(nums)]

        heapify(heap1)

        heapify(heap2)

        for i,num in enumerate(nums):
    
            while heap1 and heap1[0][1] <= i:
                heappop(heap1)

            while heap2 and ( heap2[0][1] <= i or (heap1 and heap1[0][0] == heap2[0][0])):
                heappop(heap2)
            
            if heap2:
                res.append(heap2[0][0])
            else:
                res.append(-1)

        return res



        
        m = -1
        sm = -1

        for num in reversed(nums):
            
            res.append(sm)
            
            if num >= m:
                sm = m
                m = num
            elif num >= sm:
                sm = num
            
            print(m,sm)
            
        return reversed(res)
        
        

        #rest = []
        
        #while ( nums > 0 ):
        #    nums -= 1
        
        
        mid, stk, n = [[] for _ in range(len(A))], [], len(A)
        for i in range(n):
            while stk and A[stk[-1]] < A[i]:
                mid[i].append(stk.pop())
            stk.append(i)
        print(stk)
        pq, ans = [], [-1] * len(A)
        for i in range(n):
            while pq and pq[0][0] < A[i]:
                ans[heappop(pq)[1]] = A[i]
            for j in mid[i]:
                heappush(pq, (A[j], j))
        return ans
        '''

        h = []

        heapq.heapify(h)

        A = {}

        for i in range(len(nums)):

            if h:
                td = []
                while h and h[0][0] < nums[i]:

                    x,pos, l = heappop(h)

                    l = list(l)
                    l.append(nums[i])
                    l = tuple(l)

                    td.append((x,pos, l))


                for x,y,l in td:

                    if len(l)<2:
                        heappush(h, (x,y,l))
                    if len(l)==2:
                        A[y] = l[1]

            heappush(h, (nums[i],i, ()))

        ans = [-1] * len(nums)

        for key in A:
            ans[key] = A[key]

        return ans
