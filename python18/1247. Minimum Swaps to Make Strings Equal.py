class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y, y_x = 0, 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if c1 == 'x':
                    x_y += 1
                else:
                    y_x += 1
                    
        if (x_y + y_x) % 2 == 1:
            return -1
        # Both x_y and y_x count shall either be even or odd to get the result.
		# x_y + y_x should be even
        
        res = x_y // 2
        res += y_x // 2
        
        if x_y % 2 == 1:
            res += 2
        # If there count is odd i.e. we have "xy" and "yx" situation
        # so we need 2 more swaps to make them equal
            
        return res
        
        N = len(s1)
        cx = s1.count('x') + s2.count('x')
        cy = s1.count('y') + s2.count('y')

        if cx %2 != 0:
            return -1

        d = 0
        
        s1 = [c for c in s1]
        s2 = [c for c in s2]

        ms = 0
        for i in range(N):
            if s1[i] == s2[i]:
                continue
            for j in range(i+1,N):
                if s1[i] == s2[j]:
                    d+=1
        
        return d