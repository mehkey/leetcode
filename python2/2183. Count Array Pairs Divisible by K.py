class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        c = defaultdict(int)
        t = 0
        n =len(nums)
        res = 0
        for i in nums:
            #if i % k == 0 :
            #    t += 1
            #else :
            g = gcd(k,i)
            #if g != 1:
            c[g] += 1

        for a in c:
            for b in c:
                if a <= b and a * b % k == 0:
                    res += c[a] * c[b] if a < b else c[a] * (c[a] - 1) // 2
        return res
        
        #res = t * (n-t) + factorial(t-1)  if t > 0 else 0

        #for k1 in c.keys():
        #    for k2 in c.keys():
        #        if k1 < k2 and k1 * k2 == k:
        #            res += c[k1] * c[k2]

        #for k1 in c.keys():
        #    if k1 * k1 == k :
        #        res +=  (c[k1] * (c[k1]-1)) //2

        #return int(res)

        """
        cnt = Counter(math.gcd(a, k) for a in nums)
        res = 0
        for a in cnt:
            for b in cnt:
                if a <= b and a * b % k == 0:
                    res += cnt[a] * cnt[b] if a < b else cnt[a] * (cnt[a] - 1) // 2
        return res
            
        """
        
        counter = Counter() #hashmap dicitionary of python
        ans = 0
        n = len(nums)
        
        for i in range(n):
            x = math.gcd(k,nums[i]) #ex: 10 = k and we have nums[i] as 12 so gcd will be 2
            want = k // x #what do we want from upper ex: we need 5
            for num in counter:
                if num % want == 0: #so if we find a number that is divisible by 5 then we can multiply it to 12 and make it a factor of 10 for ex we find 20 so it will be 240 which is divisible by 10 hence we will add it to answer
                    ans += counter[num] #we are adding the freq as we can find no of numbers that have same factor
            counter[x] += 1 #here we are increasing the freq of 2 so that if we find 5 next time we can add these to the answer
        return ans
        