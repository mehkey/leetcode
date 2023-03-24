class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks = sorted(tasks,key=lambda x:x[1])
        chosen_set = set()
        for task in tasks:
            cur_start,cur_end,cur_duration = task[0],task[1],task[2]
            for time in chosen_set:
                if time >= cur_start and time <=cur_end:
                    cur_duration-=1
                if cur_duration==0:
                    break
            while cur_duration>0:
                if cur_end not in chosen_set:
                    chosen_set.add(cur_end)
                    cur_duration-=1
                cur_end-=1
        return len(chosen_set)
    
    tasks.append([10 ** 9 + 1, 10 ** 9 + 1, 1]) 
    res, q = 0, []
    for s, e, d in sorted(tasks) :
        while q and q[0][0] + res < s :
            if q[0][0] + res >= q[0][1]: heappop(q) 
            else : res += min(q[0][1], s) - (q[0][0] + res)
        heappush(q, [e - d + 1 - res, e + 1])
    return res
	
    line = [0]*2001
        for i, (lo, hi, time) in enumerate(sorted(tasks, key=lambda x: x[1])): 
            cnt = sum(line[x] for x in range(lo, hi+1))
            time = max(0, time - cnt)
            for x in range(hi, lo-1, -1): 
                if time and not line[x]: 
                    line[x] = 1
                    time -= 1
        return sum(line)