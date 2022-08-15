class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        
        hm = defaultdict(int)
        day = 0

        for task in tasks:
            #day+=1
            if hm[task] == 0:
                hm[task] = float("-inf")
            
            day = max(day + 1, hm[task] + space + 1  )

            hm[task] = day
            #while hm[task] > day:
            #    day+=1
            #hm[task] = day + space
            #day+=1
        
        return day
        #return #max(hm.values()) - space
        
        """"
        heap = []
        
        if not tasks:
            return 0
        
        #heapq.heappush(h,[0,tasks[0],'s'])
        
        #h.append()
        
        day = 0
        
        i = 0
        
        h = defaultdict(int)
        
        while heap or i < len(tasks):
            
            while heap and heap[0][0] <= day:
                d, t, s = heappop(heap)

                #if s == 's':
                #    heapq.heappush(h,[day+space,tasks[i],'e'])
                #    h[t] += 1
                #else:
                print("free", t, "on day", d)
                h[t] -= 1
            
            if i < len(tasks) and h[tasks[i]] == 0:
                #print("added", i, tasks[i])
                heapq.heappush(heap,(day+space,tasks[i],'s'))
                h[tasks[i]] += 1
                i+=1
            
            day += 1
        
        return day -1
        
        count_dict = {}
        total_days = 0
        for task in tasks:
            if task not in count_dict:
                count_dict[task] = -math.inf
            total_days = max(total_days + 1, count_dict[task] + space + 1)
            count_dict[task] = total_days
        return total_days
        """
    
    
            
            