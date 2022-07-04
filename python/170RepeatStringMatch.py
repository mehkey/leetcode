class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        """        temp = ""
        count = 0
        while len(temp) < len(B):
            temp+=A
            count += 1
            if B in temp:
                return count
        temp += A
        if B in temp:
            return count + 1
        return -1"""
    
        
        cur = ""
        count = 0
        
        while len(cur) < len(b) :
            cur+=a
            count += 1
            if b in cur:
                return count
        
        cur += a
        if b in cur:
            return count + 1
        
        return -1
            #if len(cur) > len(b):
           #     return -1
            
            #if cur.index(b) == -1:
            #    cur = cur + a
            #else:
            #    return cur.index(b)
        
       # return -1