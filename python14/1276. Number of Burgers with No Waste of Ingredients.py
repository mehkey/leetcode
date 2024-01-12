class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        
        '''
        
        4T + 1C = J
        2T + 1C = S
        
        
        '''
        val = (tomatoSlices - 2*cheeseSlices)

        if val >= 0 and val%2 == 0 and cheeseSlices-val//2 >= 0:
            return [val//2,cheeseSlices-val//2]

        return []

        
        tar = cheeseSlices * 2
        
        
        res = tomatoSlices - tar
        
        if res == 0:
            return [0,cheeseSlices]
        
        if res == 0:
            return [0,cheeseSlices]
        
        tar = (cheeseSlices-1) * 4
        
        
        res = tomatoSlices - tar
        
        if res == 2:
            return [cheeseSlices-1,1]
        
        return []
        