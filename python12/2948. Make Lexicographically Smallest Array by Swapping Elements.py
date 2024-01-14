class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        '''
        h = []
        d = deque()
        
        for i,n in enumerate(nums):
            
        '''
        
        res = [0] * len(nums)
        
        hh = [(v,i) for i,v in enumerate(nums)]
        
        heapify(hh)
        
        cur = hh[0][0]
        while hh:
            
            lis = []
            lisI = []

            while hh and abs(cur - hh[0][0]) <= limit:
                v,i = heappop(hh)
                lis.append(v)
                lisI.append(i)
                cur = v

            lis.sort()
            lisI.sort()
            #print(lis)
            
            for i,v in enumerate(lis):
                res[lisI[i]] = v
            
            if hh:
                cur = hh[0][0]

        return res
            
            
            