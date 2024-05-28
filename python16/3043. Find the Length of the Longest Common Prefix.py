
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        M = len(arr1)
        N = len(arr2)

        ddd = set()
        
        eee = set()
        
        for i in range(M):
            s = str(arr1[i])
            cur = []
            
            for k in range(len(s)):
                cur.append(s[k])
                ddd.add(''.join(cur))
            
        for i in range(N):
            s = str(arr2[i])
            cur = []
            
            for k in range(len(s)):
                cur.append(s[k])
                eee.add(''.join(cur))
        
        
        res = ddd & eee
        
        #print(res, ddd, eee)
        ml = 0
        for r in res:
            ml = max(ml, len(r))
        
        return ml