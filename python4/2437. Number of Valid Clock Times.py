class Solution:
    def countTime(self, time: str) -> int:

        pot = Deque([time])
        
        while any(['?' in p for p in pot]):
            
            for _ in range(len(pot)):
                p = pot.popleft()
                if '?' in p:
                    for i in range(0,10):
                        q = p.replace('?', str(i), 1)
                        #print(q)
                        if '?' in q:
                            pot.append(q)
                            continue
                            
                        k = q.split(':')
                        if 0 <= int(k[0]) <= 23 and 0 <= int(k[1]) <= 59:
                            pot.append(q)
                else:
                    pot.append(p)
                    
        
        return len(pot)