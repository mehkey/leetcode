class Solution:
    def distributeCandies(self, n: int, lim: int) -> int:

        ans = 0

        for i in range(min(lim,n)+1):

            rest = n - i

            if rest > 2*lim:
                continue

            ans += min(rest,lim) - (rest - min(rest,lim))  + 1

        return ans


        if 3 * lim < n:
            return 0

        possibilities = math.comb(n + 2, 2)

        if n > lim:
            possibilities -= 3 * math.comb(n - lim + 1, 2)

        if n - 2 >= 2 * lim :
            possibilities += 3 * math.comb(n - 2 * lim, 2)

        return possibilities
    
        '''
        https://leetcode.com/problems/distribute-candies-among-children-ii/solutions/4276868/100-beat-o-1-detail-explanation-combination-simple-and-easy/
        if 3 * lim < n:
            return 0

        possibilities = math.comb(n + 2, 2)

        if n > lim:
            possibilities -= 3 * math.comb(n - lim + 1, 2)

        if n - 2 >= 2 * lim :
            possibilities += 3 * math.comb(n - 2 * lim, 2)

        return possibilities

        
        s = set()
        
        @cache
        def dp(c,cur):

            if cur == 0:
                if c < lim:
                    return dp(c+1,cur) + dp(0,cur+1)
                else:
                    return dp(0,cur+1)
            
            if cur == 1:
                if c < lim:
                    return dp(c+1,cur) + dp(0,cur+1)
                else:
                    return dp(0,cur+1)

            if cur == 2:
                if c < lim:
                    return dp(c+1,cur) 
                elif c == lim:
                    return 1

        return dp(0,0)
        '''