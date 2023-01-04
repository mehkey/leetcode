class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        # Countin blocks
        n, mi = len(blocks), inf
        for i in range(n - k + 1):
            white = blocks.count('W', i, i + k)
            mi = min(white, mi)
        return mi
    
        """
        def check(blocks):
            count = 0
            m = 0
            for b in blocks:
                if b == 'B':
                    count+=1
                if b == 'W':
                    count = 0
                
                m = max(m,count)
            return m
        
        self.ma = float('inf')
        
        @cache
        def bfs(blocks,i,ch):
            if ch > k:
                return
            
            blocks = list(blocks)
            if check(blocks) >= k:
                self.ma = min(self.ma,ch)
                return

            if i == len(blocks):
                return
            
            for j in range(i,len(blocks)):
                b = blocks[j]
                if b == 'W':
                    blocks[j] = 'B'
                    bfs(str(blocks),j+1,ch+1)
                    blocks[j] = 'W'
        
        
        bfs(blocks,0, 0)
        return self.ma
        
        
        ans = 0
        res = 0

        for i in range(len(blocks) - k + 1):
            res = blocks.count('B', i, i + k)
            ans = max(res, ans)

        ans = k - ans
        return ans
        
        
        #for b in blocks:
        def check(blocks):
            count = 0
            m = 0
            for b in blocks:
                if b == 'B':
                    count+=1
                if b == 'W':
                    count = 0
                
                m = max(m,count)
            return m
        
        self.ma = float('inf')
        
        @cache
        def bfs(blocks,i,ch):
            blocks = list(blocks)
            if check(blocks) >= k:
                self.ma = min(self.ma,ch)
                return

            if i == len(blocks):
                return
            
            for j in range(i,len(blocks)):
                b = blocks[j]
                if b == 'W':
                    blocks[j] = 'B'
                    bfs(str(blocks),j+1,ch+1)
                    blocks[j] = 'W'
        
        
        bfs(blocks,0, 0)
        return self.ma
        
        
        def check(blocks):
            count = 0
            m = 0
            for b in blocks:
                if b == 'B':
                    count+=1
                if b == 'W':
                    count = 0
                
                m = max(m,count)
            return m
        
        blocks = list(blocks)
        
        
        while check(blocks) < k:
            #counts = [(x, len(list(group))
            #      for x, group in itertools.groupby(blocks)]
                       
            #counts = [(x, len(list(group)))
            #  for x, group in itertools.groupby(A)]
            
            #for i,c in enumerate
            
            for i,c in enumerate(blocks):
                if blocks == b:
                    blocks += 1
            
            
            m = 0
            j = 0
            for i,c in enumerate(counts):
                if c[0] == 'W':
                    num = c[1] + (counts[i-1][1] if i>0 else 0) + (counts[i+1][1] if i < len(counts)-1 else 0)
                    if num > m:
                        m = num
                        j = i
                
            counts
            
        
        #for c in counts:
        #    if c[0] == 'W':
        #       count -= 1
        
        #print(counts)
        
        #for i i
        """