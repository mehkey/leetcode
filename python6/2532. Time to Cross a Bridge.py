'''
class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:

        h = []

        for i,w in enumerate(time):
            h.append((0,-(w[0]+w[2]),-i,w))

        heapify(h)

        box = 0
        time = 0

        waiting = True

        r_h = []

        t = 0

        while True:

            if (r_h and h and r_h[0][0] < h[0][0]) or (r_h and not h) or (r_h and box==n):
                cur = heappop(r_h)
                #print(cur)
                c_t = cur[0]

                

                c_eff = cur[1]
                c_i = cur[2]
                
                c_l = cur[3]

                time = max( time, t +c_l[2])

                if c_t > t:
                    t = c_t

                if box != n:
                    print(c_i)
                    heappush(h, (t+c_l[3]+c_l[2], c_eff, c_i, c_l))


            if h and box != n:

                cur = heappop(h)
                #print(cur)
                c_t = cur[0]
                
                

                c_eff = cur[1]
                c_i = cur[2]
                

                c_l = cur[3]
                
                if c_t > t:
                    t = c_t + c_l[0]
                else:
                    t = t + c_l[0]
                    
                if box != n:
                    print(c_i)
                    heappush(r_h, (t+c_l[0]+c_l[1], c_eff, c_i, c_l))

                    box += 1
                
            else:
                print("ERROR: all heap is empty", h, r_h)

            t+=1

            if box == n and not r_h:
                break

        return time
'''

class Solution:
    def findCrossingTime(self, n: int, k: int, time) -> int:
        # at the beginning everyone is waiting on the left
        lwait = [(-(x[0] + x[2]), -i) for i, x in enumerate(time)]
        heapify(lwait)
        
        rwait = []
        picklist = []  # (time, i) heap
        putlist = []  # (time, i) heap
        
        T = 0
        bridgeEmptyTime = 0
        while True:
            T = max(T, bridgeEmptyTime)
            
            # the bridge is empty & no box on the right => we're done here
            if n == 0:
                return T

            # maybe everyone is picking or putting a box
            # we have to make sure at least one person is waiting to pass the bridge
            
            tmp = []
            if picklist:
                tmp.append(picklist[0][0])
            if putlist:
                tmp.append(putlist[0][0])
            if not rwait and not lwait and T < min(tmp):
                T = min(tmp)
            
            # release everyone who finished picking or putting
            while picklist and T >= picklist[0][0]:
                i = heappop(picklist)[1]
                heappush(rwait, (-(time[i][0] + time[i][2]), -i))
            
            while putlist and T >= putlist[0][0]:
                i = heappop(putlist)[1]
                heappush(lwait, (-(time[i][0] + time[i][2]), -i))

            # people on the right go first
            if rwait:
                i = -heappop(rwait)[1]
                n -= 1
                bridgeEmptyTime = T + time[i][2]
                heappush(putlist, (bridgeEmptyTime + time[i][3], i))
            # all boxes are taken, nobody needs to pass the bridge from left to right
            elif len(picklist) == n:
                T = picklist[0][0]
            else:
                i = -heappop(lwait)[1]
                bridgeEmptyTime = T + time[i][0]
                heappush(picklist, (bridgeEmptyTime + time[i][1], i))