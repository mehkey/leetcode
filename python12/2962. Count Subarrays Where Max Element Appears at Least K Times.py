'''

13233

1

13

132

1323 (1 1323. 2 13233)

323.  (1 323.  232)     


'''

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        h = []
        mm = max(nums)

        hm = defaultdict(int)
        l = 0
        res = 0
        s = set()
        
        for r in range(0,n):
            
            hm[nums[r]] += 1

            #if nums[r] not in s:
            #    s.add(nums[r])
            #    heappush(h,-nums[r])
            #print(hm)
            #print(h)
            #print(s)
            while l < n and hm[mm] >= k: #h and hm[-h[0]] >= k:
                
                res += n - r
                #print('add', n-r)

                hm[nums[l]] -=1

                #while h and hm[-h[0]] == 0:
                #    s.remove(-h[0])
                #    heappop(h)
                
                #print('now', h, hm)
                l += 1

        return res

            