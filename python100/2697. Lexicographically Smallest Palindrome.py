class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        
        c = 0
        mid = len(s) // 2
        
        res = [c for c in s]


        l = 0
        r = len(s) -1
        
        while l<r:
            if s[l] != s[r]:
                c+=1
                if s[l] < s[r]:
                    res[r] = s[l]
                else:
                    res[l] = s[r]
            
            l+=1
            r-=1

            
        '''
        for i in range(0,len(s)//2 ):
            
            if s[mid - i] != s[mid +i]:
                c+=1
                if s[mid - i] < s[mid +i]:
                    res[mid +i] = s[mid - i]
                else:
                    res[mid - i] = s[mid +i]

        '''
        return ''.join(res)