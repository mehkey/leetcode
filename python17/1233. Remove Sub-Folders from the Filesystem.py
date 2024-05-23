class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        '''
        G = defaultdict(list)
        
        for f in folder:
            
            f = f.split('/')
            
            for i in range(1,len(f)-1):
                G[f[i]].append(f[i+1])
        
        
        def dfs():
            
        '''
        # s = set(folder)
        
        res = []
        
        for f in folder:
            #j = f
            f = f.split('/')
            cur = []
            
            found = False
            for i in range(1,len(f)-1):
                cur.append('/' + f[i])
                if ''.join(cur) in s:
                    found = True
                    break
            if not found:
                res.append(f)
        return res