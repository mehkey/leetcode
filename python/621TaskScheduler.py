class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #O(n)
        count = Counter(tasks)
        
        #print(count)
        hm = []
        for k in count:
            hm.append( -count[k])
        
        #O(n)
        heap = heapq.heapify(hm)
        
        
        time = 0
        
        queue = deque()
        
        while True:
            time += 1
            #print(time)
            #print(hm)
            #print(queue)
            if hm:
                v = heapq.heappop(hm)
                
                if (v + 1)< 0:
                    queue.append([v+1,time+n])
            #print(queue)
            if queue and queue[0][1] == time:
                v,t = queue.popleft()

                
                heapq.heappush(hm,v)
                
            
            if not hm and not queue :
                break
        
        return time