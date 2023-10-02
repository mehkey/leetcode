class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        
        temp = moves[::]
        
        res = temp.replace('_','R')
        res1 = temp.replace('_','L')
        print(res)

        s = 0
        
        for m in res:
            if m == 'L':
                s -= 1
            else:
                s += 1
        
        
        s1 = 0
        
        for m in res1:
            if m == 'L':
                s1 -= 1
            else:
                s1 += 1
        
        return max(abs(s),abs(s1))
