class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        
        hm = defaultdict(int)
        
        cur = 0
        for log in logs:

            hm[log[0]] = max(log[1]-cur, hm[log[0]])
            
            cur = log[1]

        m = max(hm.values())
        
        for h in sorted(hm.keys()):
            if hm[h] == m:
                return h
