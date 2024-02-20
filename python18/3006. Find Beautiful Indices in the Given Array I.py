class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        
        
        N = len(s)
        A = len(a)
        B = len(b)

        aa = [0]* N
        
        bb = [0]* N


        for i in range(N-A+1):
            
            if s[i:i+A] == a:
                aa[i] = 1
    
        for i in range(N-B+1):
            
            if s[i:i+B] == b:
                bb[i] = 1
        
        count = 0
        
        for i in range(min(k+1,N)):
            if bb[i]:
                count += 1
        
        res = []

        for i in range(N-A+1):
            if i - k -1 >= 0 and bb[i - k -1]:
                count -= 1
            
            if aa[i] and count > 0:
                res.append(i)
            
            if i + k+1 < N and bb[i+k+1]:
                count += 1
        
        return res
            