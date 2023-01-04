from sortedcontainers import SortedList

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        
        
        n = len(nums)
        prefix = list(accumulate(nums))
        sl = SortedList([-1,n])
        #print(prefix)
        prefix  = [0] + prefix
        #print(prefix)
        mp = {-1 : n}
        h = []
        res = []

        h.append( (-prefix[-1], 0,len(nums)-1))
        
        rem = set()
        
        for q in removeQueries:
            
            sl.add(q)
            
            i = sl.bisect_left( q)
            lo = sl[i-1]
            hi = sl[i+1]
            
            heappush(h, (-(prefix[q]-prefix[lo+1]), lo, q))
            heappush(h, (-(prefix[hi]-prefix[q+1]), q, hi))
            
            print(h)
            
            mp[lo] = q
            mp[q] = hi 
            print(mp)
            while mp[h[0][1]] != h[0][2]: heappop(h)
            res.append(-h[0][0])
            
            print(h)
            
        return res

        """n = len(nums)
        sl = SortedList([-1, n])
        prefix = list(accumulate(nums, initial=0))
        mp = {-1 : n}
        pq = [(-prefix[-1], -1, n)]

        ans = []
        for q in removeQueries: 
            print(mp)
            sl.add(q)
            print(sl)
            i = sl.bisect_left(q)
            lo = sl[i-1]
            hi = sl[i+1]
            mp[lo] = q
            mp[q] = hi 
            heappush(pq, (-(prefix[q]-prefix[lo+1]), lo, q))
            heappush(pq, (-(prefix[hi]-prefix[q+1]), q, hi))

            while mp[pq[0][1]] != pq[0][2]: heappop(pq)
            ans.append(-pq[0][0])

        return ans

        """

        