PL = set()

for j in range(10):
    PL.add(j)

for i in range(1,10**5):
    
    s = str(i)
    sr = s[::-1]
    for j in range(10):
        
        cand = s + str(j) + sr
    
        cand = int(cand)
        PL.add(cand)
    

    cand = s + sr

    cand = int(cand)
    PL.add(cand)
PL = sorted(PL)

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        #print(PL)
        
        mid = median(nums)
        
        def cal(mmm):
            res = 0
            for n in nums:
                res += abs(mmm - n)
            return res

        FL = mid
        FR = mid
        FLM = inf
        FRM = inf

        i = 0
        while PL[i] < mid:
            i+=1
        #print(PL[i])
        #print(PL[i-1], cal(PL[i]) ,cal(PL[i-1]), cal(PL[i+1]))
        return min( cal(PL[i]) ,cal(PL[i-1]), cal(PL[i+1]) )

        '''
        mvv = max(nums)
        #vm = max(10**( len(str(mvv)) - 2) ,1000 )
        vm = 1000_000
        while v<vm and FL > 0:
            #FL = mid
            if isP(FL):
            #    break
                FLM = min(FLM,cal(FL))
            FL -= 1
            v+=1
        v = 0
        while v < vm:
            #FL = mid
            if isP(FR):
            #    break
                FRM = min(FRM,cal(FR))
            FR += 1
            v+=1
        
        
        
        l = 0
        r = 10**9
        
        mc = 0
        
        def cal(mid):
            res = 0
            for n in nums:
                res += abs(mid - n)
            return res
        
        def isP(num):
            i = 0
            b = str(num)
            N = len(b)

            while i < len(b):
                if b[i] != b[N-i-1]:
                    return False
                i+=1
            return True

        #mid = median(nums)
        mid = sum(nums)//len(nums)
        #print(mid)
        FL = mid
        FR = mid
        FLM = inf
        FRM = inf
        v = 0
        mvv = max(nums)
        #vm = max(10**( len(str(mvv)) - 2) ,1000 )
        vm = 1000_000
        while v<vm and FL > 0:
            #FL = mid
            if isP(FL):
            #    break
                FLM = min(FLM,cal(FL))
            FL -= 1
            v+=1
        v = 0
        while v < vm:
            #FL = mid
            if isP(FR):
            #    break
                FRM = min(FRM,cal(FR))
            FR += 1
            v+=1
        #print(FL,FR)
        mmm = inf
        for i in range(0,10):
            mmm = min(cal(i),mmm)
        #return min(cal(FL), cal(FR),mmm)
        #print(FRM, FLM,mmm)
        return min(FRM, FLM,mmm)
        '''