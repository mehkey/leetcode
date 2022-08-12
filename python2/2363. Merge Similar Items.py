#import SortedDict
from sortedcontainers import SortedList

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        #n = len(items1
        #items1 = sorted(items1, )
        #for i in range(n)
        
        #o =sortedcontainers(items1)
        #print(c)
        
        cnt = Counter()
        for v, w in items1 + items2:
           cnt[v] += w
        return sorted(cnt.items())
        
        #s = Counter(SortedList(items1 + items2))
        #return Counter(SortedList(items1 + items2)).items()
        #print(s)
        
        #c1 = Counter(dict(items1))
        #c2 = Counter(dict(items2))
        
        return sorted( (Counter(dict(items1))+Counter(dict(items2))).items())
        
        #s += 1
        
        #s -= 2
        #res = []
        #cur = 0
        #for i in range(len(s)-1):
        #    if s[i][0] == s[i+1][0]:
        #        cur += s[i][1]
        #    else:
        #        res.append([s[i][0],cur+s[i][1]])
        #        cur = 0
        
        #if cur != 0:
        #    res.append([s[-1][0],cur])
        
        #return res
        #print(items1 + items2)
        
        #print(dict(items1 + items2) )

        #o = OrderedDict(  dict(items1) )

        #o = o | OrderedDict(  dict(items2) )

        #return o.items()

        # print(o)
        """items1 = sorted(items1, key=lambda x: x[0])
        
        items2 = sorted(items2, key=lambda x: x[0])
        
        #print(items1)
        #print(items2)
        
        #c = Counter(items1, )
        
        res = []
        
        #items1.append([float("inf"),0])
        #items2.append([float("inf"),0])
        
        i = j = 0
        
        while i < len(items1) or j < len(items2):
            
            if i == (len(items1)):
                res.append([items2[j][0],items2[j][1] ])
                j+= 1
                continue
            elif j == len(items2):
                res.append([items1[i][0],items1[i][1] ])
                i+=1
                continue
            
            if items1[i][0] ==items2[j][0]:
                res.append([items1[i][0],items1[i][1] +items2[j][1] ])
                i+=1
                j+=1
            elif items1[i][0] < items2[j][0]:
                res.append([items1[i][0],items1[i][1] ])
                i+=1
            else:
                res.append([items2[j][0],items2[j][1] ])
                j+= 1
        return res"""
            