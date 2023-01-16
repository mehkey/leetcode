class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        

        n = len(nums)
        hm = defaultdict(int)
        l = 0
        q = deque()
        res = 0
        

        count = 0
        
        for i,r in enumerate(nums):
            hm[r] += 1
            if hm[r]== 2:
                count += 1
            else:

                count += hm[r]-1

            q.append(r)
            
            while q and count >= k:

                bad = q.popleft()
                hm[bad] -=1
                if hm[bad] == 1:
                    count -= 1
                elif hm[bad] >= 2:

                    
                    count -= hm[bad]
                
                res += ( n-i)
        
        return res
            
            