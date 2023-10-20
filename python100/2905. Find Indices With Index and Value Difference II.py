#from segment_tree import SegmentTree

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:


for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) >= valueDifference and abs(i - j) >= indexDifference:
                    return [i, j]
        return [-1, -1]


        c =  Counter() #SegmentTree() #Counter()
        ma = []
        mi = []
        
        n = len(nums)
        
        for i in range(indexDifference,n):
            c[nums[i]] += 1
            heappush(mi, (nums[i],i))
            heappush(ma, (-nums[i],i))

        for i in range(0,n):
            
            while mi and abs(mi[0][1] - i) <  indexDifference:
                heappop(mi)

            while ma and abs(ma[0][1] - i) <  indexDifference:
                heappop(ma)
            
            if mi and abs(mi[0][0] - nums[i]) >= valueDifference:
                return [i,mi[0][1]]
                
            if ma and abs(-ma[0][0] - nums[i]) >= valueDifference:
                return [i,ma[0][1]]
            
            if i + indexDifference + 1 < n:
                j = i + indexDifference + 1 
                c[nums[j]] += 1
                heappush(mi, (nums[j],j))
                heappush(ma, (-nums[j],j))
            
            if i - indexDifference  >= 0:
                j = i - indexDifference 
                c[nums[j]] -= 1
                #heappush(mi, (nums[j],j))
                #heappush(ma, (-nums[j],j))
            
        '''
            
        for i in range(indexDifference,indexDifference-n):
            if abs(mi[0][0] - nums[i]) >= valueDifference:
                return [i,mi[0][1]]

            if abs(-ma[0][0] - nums[i]) >= valueDifference:
                return [i,ma[0][1]]

            if i + indexDifference + 1 < n:
                j = i + indexDifference + 1 
                c[nums[j]] += 1
                heappush(mi, (nums[j],j))
                heappush(ma, (-nums[j],j))
        '''

        return [-1,-1]



