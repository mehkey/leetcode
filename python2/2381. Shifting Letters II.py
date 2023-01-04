class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        
        c = [[0,0]] * (len(shifts) *2)
        i = 0
        for f,e,d in shifts:
            c[i] = [f,1 if d == 1 else -1]
            i+=1
            c[i] = [e+1,-1 if d == 1 else 1]
            i+=1
        print(c)
        c.sort()
        res = ''
        j = 0
        add = 0
        
        for i,l in enumerate(s):
            
            while j < len(c) and i == c[j][0] :
                add += c[j][1]
                j+=1

            res +=  chr((ord(s[i]) + add - ord('a'))  %26 + ord('a'))
        
        return res
        
        """
        #Segment
        for f,e,d in shifts:
            for i in range(f,e+1):
                if d == 0:
                    shif[i] -=1
                if d == 1:
                    shif[i] +=1
        
        res = [''] * len(s)
        #print(ord('a'))
        for i,f in enumerate(shif):
            #print(ord(s[i]))
            #print(chr( (ord(s[i]) + f) %26 ))
            
            #print( (ord(s[i]) + f - ord('a'))  %26 + ord('a') )
            #print( chr((ord(s[i]) + f - ord('a'))  %26 + ord('a')))
            
            res[i] = chr((ord(s[i]) + f - ord('a'))  %26 + ord('a'))
        
        #print(res)
        
        """
        
        return ''.join(res)