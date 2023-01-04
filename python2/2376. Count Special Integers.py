class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        

        def countUnique( n) :
            if (n < 1): return 0
            cur = 9
            nine = 9
            while(n-1 > 0) :
                if (nine == 0) :
                    return 0
                cur = cur* nine
                nine-=1
                n -=1
            return cur
        
        
        def isUniqueDigits( n) :
            u = set()
            if (n < 10) :
                return True;
            while (n > 0) :
                digit = n % 10;
                if digit in u:
                    return False;
                u.add(digit)
                n = n // 10;

            return True

        used = defaultdict(int)
        
        s = str(n)
            
        res = 0
        
        N = len(s)
            
        
        for i in range(1,N):

            res += countUnique(i)
        
        res += (int(s[0]) -1) * factorial(9) // factorial( 9 - N + 1)

        used[int(s[0])] = 1
        
                
        for i in range(1,N):
            count = 0
            for j in range(0,int(s[i])):
                if used[j] != 1:
                    count+=1
            res += count * factorial(9-i) // factorial(9 - N + 1)
                        
            used[int(s[i])] = 1

        
        if (isUniqueDigits(n)) :
            res += 1;

        return res

