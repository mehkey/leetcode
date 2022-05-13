class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        pair = [[p,s] for p, s in zip(position,speed)]
        
        pair = sorted(pair, reverse=True)
        
        fleetarrivetime = sys.maxsize

        res = 1
        
        for i in range(len(pair)):
            
            p,s = pair[i]
            
            #print(p, " ", s)
            arriveTime = (target - p) / s
            
            if fleetarrivetime == sys.maxsize:
                fleetarrivetime = arriveTime
            else:
                
                if arriveTime > fleetarrivetime:
                   
                    fleetarrivetime = arriveTime
                    res += 1 #new fleet
        
        return res
            
            
        
        
        
        