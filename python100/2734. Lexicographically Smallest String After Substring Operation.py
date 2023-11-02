class Solution:
    def smallestString(self, s: str) -> str:
        
        first= -1
        
        ind = 0
        
        while ind < len(s):
            if s[ind] == 'a':
                ind+=1
            else:
                break
        
        if ind == len(s):
            res = [c for c in s]
            res[-1] = 'z'
            return "".join(res)

        end = ind
        while end < len(s):
            if s[end] != 'a':
                end+=1
            else:
                break
        
        #print(ind,end)
        res = [c for c in s]

        for i in range(ind,end):
            res[i] = chr(ord(res[i]) -1)
        
        return "".join(res)

            