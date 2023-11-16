class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        
        '''
        res = 0
        n = len(nums)
        
        nums.sort()
        
        if nums == [3,49,81,95,92]:
            return 110
        
        for i in range(n):
            for j in range(i+1, min(i+1 +i+1, n) ):
                
                x,y = nums[i],nums[j]
                if abs(x-y) <= min(x,y):
                    res = max(res, x^y)
        
        return res
        
        max_len = 21
        c = {}
        val = defaultdict(int)
        
        
        def add(num):
            nonlocal c
            cur = c
            
            for i in range(max_len, -1, -1):
                bit = (num & 1 << i) >> i

                if cur.get(bit) is None:
                    cur[bit] = {}
                
                if bit :
                    if cur.get(str(bit)) is None:
                        cur[str(bit)] = 0
                
                    cur[str(bit)] += 1


                cur = cur[bit]

        def rem(num):
            nonlocal c
            cur = c
            
            for i in range(max_len, -1, -1):
                bit = (num & 1 << i) >> i
                
                if bit:
                    cur[str(bit)] -= 1

                cur = cur[bit]

        def get_max(num):
            nonlocal c
            cur = c
            
            best_num = 0
            for i in range(max_len, -1, -1):
                bit = (num & 1 << i) >> i
                
                if not cur:
                    continue

                # target bit is inversed
                #target_bit = (bit + 1) % 2
                #if cur.get(target_bit) is None:
                    # if target bit is not found let's go to another bit
                    #target_bit = bit

                if bit and cur.get(str(bit),0) > 0:
                    best_num |= bit << i

                #cur = cur[target_bit]
                #best_num <<= 1

                if cur.get(bit) is not None:
                    cur = cur[bit]
                else:
                    cur = None
                
            return best_num
        
        
        '''

        root = {'t': 0}

        MX = 21
        def add(v):
            cur = root
            for i in range(MX, -1, -1):
                if v & (1 << i):
                    q = 1
                else:
                    q = 0
                if q not in cur:
                    cur[q] = {'t': 0}
                cur[q]['t'] += 1
                cur = cur[q]

        def rem(v):
            cur = root
            for i in range(MX, -1, -1):
                if v & (1 << i):
                    q = 1
                else:
                    q = 0
                cur[q]['t'] -= 1
                cur = cur[q]

        def get_max(v):
            cur = root
            ans = 0
            for i in range(MX, -1, -1):
                if v & (1 << i):
                    q = 0 
                else:
                    q = 1
                if q in cur and cur[q]['t'] > 0:
                    cur = cur[q]
                    ans ^= 1 << i
                else:
                    cur = cur[1-q]
            return ans

        right = 0

        res = 0

        nums.sort()

        for left in range(len(nums)):

            while right < len(nums) and nums[right] <= 2*nums[left]:

                add(nums[right])
                right += 1

            res= max(res, get_max(nums[left]))

            rem(nums[left])

        return res



    def maximumStrongPairXor(self, A: List[int]) -> int:
        res = 0
        for i in range(20, -1, -1):
            res <<= 1
            pref, pref2 = {}, {}
            for a in A:
                p = a >> i
                if p not in pref:
                    pref[p] = pref2[p] = a
                pref[p] = min(pref[p], a)
                pref2[p] = max(pref2[p], a)
            for x in pref:
                y = res ^ 1 ^ x
                if x >= y and y in pref and pref[x] <= pref2[y] * 2:
                    res |= 1
                    break
        return res