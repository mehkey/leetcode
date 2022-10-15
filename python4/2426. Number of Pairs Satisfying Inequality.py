from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        #diff = [nums1[j] - nums2[j] for j in range(len(nums1))]
        
        l = SortedList()
        res = 0
        for a,b in zip(nums1, nums2):
            #print(l)
            d = a - b + diff
            #print(diff)
            add = l.bisect_right(d)
            #print(add)
            res += add
            l.add(a - b)
        return res
        
        #diff1 = [nums1[j] - nums2[j] for j in range(len(nums1))]
        
        #print(diff1)
        
        #diff2 = [nums2[j] - nums2[i] for j in range(len(nums1))]
        
        

        #print(diff)
        
        #acc1 = list(accumulate(nums1))
        
        #acc2 = list(accumulate(nums2))
        
        #print(acc1)
        
        #print(acc2)
        
        #acc1 = list(accumulate(nums1))
        
        #acc2 = list(accumulate(nums2))
        
        #n = len(nums1)
        
        #total = 0
        
        #for i in range(n):
        #    for j in range(i+1,n):
        #        if nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff:
        #            total += 1
        
        #return total
        