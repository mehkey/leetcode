class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        tasks.sort(reverse=True)
        processorTime.sort()
        pt = deque(processorTime)

        #print(pt)
        #print(tasks)

        et = 0

        i = 0
        ct = 0
        cur = 0
        
        while i < len(tasks):
            cur = 0
            
            ct = pt.popleft()
            
            cur = max(cur, tasks[i])
            i += 1
            if i == len(tasks):
                continue
            
            cur = max(cur, tasks[i])
            i += 1
            if i == len(tasks):
                continue
            
            cur = max(cur, tasks[i])
            i += 1
            if i == len(tasks):
                continue
            
            cur = max(cur, tasks[i])
            i += 1
            if i == len(tasks):
                continue
            
            pt.append(ct + cur)
            et = max(ct + cur, et)
        
        et = max(ct + cur, et)

        return et
        
            