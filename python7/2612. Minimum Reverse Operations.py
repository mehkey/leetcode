class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        
        ans = [-1] * n
        
        ans[p] = 0
        
        l = 0
        
        r = n -1
        
        bs = set(banned)
        #for b in banned:
        #    ans[b] = -1
        N = n
        if k == 1:
            return ans
        
        q = deque()
        
        q.append(p)
        
        v = set()
        
        while q:
            
            cur = q.popleft()
            
            v.add(cur)
            
            for i in range(max(cur+1,k-1), min(cur+k,N)):
                if i not in bs and i not in v:
                    q.append(i)
                    ans[i] = ans[cur] +1
                    v.add(i)
        
        q = deque()
        
        q.append(p)
        
        v = set()
        
        while q:
            
            cur = q.popleft()
            v.add(cur)
            for i in range(cur-1, max(cur-k-1,-1),-1):
                if i not in bs and i not in v:
                    q.append(i)
                    ans[i] = ans[cur] +1
                    v.add(i)
        
        return ans
        
        
        '''
        for i in range( p+1, n):
            #a = ans[]
            if i in bs:
                continue
            if i == p:
                continue
            else:
                for start in range(max(0,p+(k-1)//2, N-k-1)):
                    #temp = ans[start:start+k]
                    if start not in bs and start-k-1 >=0:
                        ans[start] = ans[start-k-1] + 1
        
                                   
        for i in range( p-1, -1,-1):
            if i in bs:
                continue
            if i == p:
                continue
            else:
                for start in range(N-1,min(p-(k-1)//2,-1), -1):
                    if start not in bs and start+k-1 < N:
                        ans[start] = ans[start+k-1] + 1
        
        return ans
        
        dist = abs(p-i)
        if dist % (k-1) != 0:
            continue

        if i > p:
            c = 0
            j = i
            while i > p:
                i -= k -1
                c+=1
                if i in bs:
                    break

            #if i == p  :
            #    ans[j] = c
            #if k%2 == 0 and (i - p) in [ o for o in range(1, k, 2)] :
            #    ans[j] = c
            #if k%2 == 1 and (i - p) in [ o for o in range(2, k, 2)] :
            #    ans[j] = c

        if i < p:
            c = 0
            j = i
            while i < p:
                i += k -1
                c+=1
                if i in bs:
                    break
            if i == p:
                ans[j] = c

            #print([ o for o in range(1, k, 2)])
            #if k%2 == 0 and (p-i) in [ o for o in range(1, k, 2)] :
            #    ans[j] = c
            #if k%2 == 1 and (p-i) in [ o for o in range(2, k, 2)] :
            #    ans[j] = c
        '''
            
        #return ans
class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        out = [-1] * n
        # To speed up iterations, mark banned positions differently; remember to
        # convert them to -1 at the end.
        for node in banned:
            out[node] = -2
        # Perform reversals in level-based breadth-first order.
        nodes = [p]
        depth = 0
        out[p] = depth
        step = k - 1
        
        # TLEs occur when n is large, k is large, and not to many are banned,
        # so that very O(N) points have O(N) possible post-reverse positions.
        # These O(N) post-reverse positions are 2 apart, but each only needs
        # to be visited once. We will nextNode2s dynamically to save work.
        nextNode2s = [i + 2 for i in range(n)]  # might be out of range

        while nodes:
            depth += 1
            newNodes = []
            for node1 in nodes:
                # The post-reverse positions are every other node between
                # loNode2 and hiNode2, inclusive.
                loReverseStart = max(node1 - step, 0)
                hiReverseStart = min(node1, n - k) # Inclusive
                loNode2 = 2 * loReverseStart + k - 1 - node1
                hiNode2 = 2 * hiReverseStart + k - 1 - node1  # Inclusive
                # We will exclude the entire range from future iterations
                # by setting nextNode2s[node2] to hiNode2 + 2 for every
                # visited node2.
                postHiNode2 = hiNode2 + 2
                node2 = loNode2
                while node2 <= hiNode2:
                    nextNode2 = nextNode2s[node2]
                    nextNode2s[node2] = postHiNode2
                    if node2 >= 0 and node2 < n and out[node2] == -1:
                        newNodes.append(node2)
                        out[node2] = depth
                    node2 = nextNode2
            nodes = newNodes
            
        # Mark all banned positions as -1 (see above).
        for i in range(n):
            if out[i] == -2:
                out[i] = -1
        return out
        