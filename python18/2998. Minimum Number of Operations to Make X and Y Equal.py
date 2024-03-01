class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        
        vis = set()
        
        q= deque()
        #vis.add(0)
        q.append(x)

        step = -1
        
        while q:
            
            step += 1
            ql = len(q)
            #print(' ')
            for _ in range(ql):
                cur = q.popleft()
                
                
                if cur == y:
                    return step
                
                if cur < 1:
                    continue

                if cur > max(x,y) + 11:
                    continue

                if cur in vis:
                    continue
                #print(cur)
                vis.add(cur)

                #for i in range(1,11):
                #res = min(res,dfs(cur+i, step+i)+i)
                #res = min(res,dfs(cur-i, step+i)+i)

                q.append(cur+1)
                q.append(cur-1)

                #res = min(res,dfs(cur+1, step+1)+1)
                #res = min(res,dfs(cur-1, step+1)+1)

                if cur % 5 == 0:
                    q.append(cur//5)
                    #res = min(res,dfs(cur//5, step+1)+1 )

                if cur % 11 == 0:
                    q.append(cur//11)
                    #res = min(res, dfs(cur//11, step+1)+1 )

        return -1
