class Solution:
    def makeStringsEqual(self, s: str, t: str) -> bool:
        
        '''

        
        1 to a 1 makes 0
        1 to a 0 makes 1
        0 to a 0 makes 0
        0 to a 1 makes 1
        
        '''

        ss = set(s)
        tt = set(t)

        if '1' in tt :
            if '1' in ss:
                return True
            return False

        if '0' in tt:
            if all([ p == '0' for p in ss]):
                return True
            return False


