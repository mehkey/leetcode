class Solution:
    def largestPalindromic(self, s: str) -> str:
        count = Counter(s)

        s = sorted(count.items())
        
        start = -1
        for p in s[::-1]:
            if int(p[1]) %2 == 1:
                start = int(p[0])
                break
        
        res = ''
        
        if start != -1:
            res = res + str(start)

        oldres = res
        for p in s:
            
            for i in range( (p[1] - 1) //2 if p[1]%2 ==1 else p[1]//2):
                res = str(p[0]) + res + str(p[0])
        
        if all(i == '0' for i in res): #res[0] == '0' and res[-1] == '0':
            return '0'

        
        if res[0] == '0':
            res = oldres
            
        
        return res

        def largestPalindromic(self, num: str) -> str:
            count = Counter(num)
            res = ''.join(count[i] // 2 * i for i in '9876543210').lstrip('0')
            mid = max(count[i] % 2 * i for i in count)
            return (res + mid + res[::-1]) or '0'

        
        """
        res = ""

        if(len(s) <= 1):
            return s
        
        if(len(s) == 2):
            return  s if s[0] == s[1] else s[0]
        
        for i in range(0, len(s)):
            
            
            def sub(l,r,res):
                while  l >= 0 and r < len(s) and s[l] == s[r] :
                    if (r - l + 1) > len(res):
                        res = s[l:r+1]
                    l -= 1
                    r += 1
                return res

            res = sub(i,i,res)
            res = sub(i,i+1,res)

        return res
        
        """