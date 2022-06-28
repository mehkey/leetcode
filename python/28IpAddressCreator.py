class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
               
        res = set()
        @lru_cache(None)
        def dfs(start, cur, count):
            
            #print('start', start, ' cur', cur, 'count', count)
            if count == 4 and  len(start) == 0 :
                res.add(cur[:-1])
                return

            if count >= 4:
                return
            
            for i in range(1,min(len(start)+1,4)):
                substart = start[i:]
                newcur =  start[:i]
                #print(substart)
                #print(newcur)
                if 0 <= int(newcur) <= 255 and not (len(newcur) > 1 and newcur[0] == '0') :
                    dfs(substart,cur + (newcur)+'.',count+1)

        dfs(s,'',0)
        
        return res