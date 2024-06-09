class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        busy=[]
        available=[i for i in range(n)]
        count=[0]*n
        meetings.sort()
        for start,end in meetings:
            while busy and busy[0][0]<=start:
                _end,room=heapq.heappop(busy)
                heapq.heappush(available,room)

            if available:
                room=heapq.heappop(available)
                heapq.heappush(busy,(end,room))
            else:
                time,room=heapq.heappop(busy)
                heapq.heappush(busy,(time+end-start,room))
            count[room]+=1
        return count.index(max(count))  

        
        
        ans = [0] * n
        times = [0] * n
        meetings.sort()

        for start, end in meetings:
            flag = False
            minind = -1
            val = float('inf')
            for j in range(n):
                if times[j] < val:
                    val = times[j]
                    minind = j
                if times[j] <= start:
                    flag = True
                    ans[j] += 1
                    times[j] = end
                    break
            if not flag:
                ans[minind] += 1
                times[minind] += (end - start)

        maxi = -1
        id = -1
        for i in range(n):
            if ans[i] > maxi:
                maxi = ans[i]
                id = i
        return id