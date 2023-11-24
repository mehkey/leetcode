from datetime import time
class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:

        hm = defaultdict(list)

        for e,t in access_times:
            hm[e].append(t)

        res = []
        for k,v in hm.items():

            v.sort()

            #print(k,v)
            tt = 0
            for i in range(2,len(v)):
                h = v[i][:2]
                m = v[i][2:]
                t1 = datetime.datetime(2020,2,2,int(h),int(m))
                h = v[i-2][:2]
                m = v[i-2][2:]
                t2 = datetime.datetime(2020,2,2,int(h),int(m))
                #print(t1,t2)
                d = t1 - t2 
                if d.total_seconds() / 60 < 60:
                    #print(k,d.total_seconds() / 60)
                    res.append(k)
                    break

        return res
