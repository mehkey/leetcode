class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        allsets = set()
        
        #curmap
        
        result = set()
        
        #for i in range(0,10):
            #curmap[s[i]] = curmap.get(s[i],0) + 1
        #curmap = s[0:10]
        
        #allsets.add(curmap)
            
        for i in range(len(s) - 9):

            #curmap[s[i]] = curmap.get(s[i],0) + 1

            #curmap[s[i-10]] = curmap.get(s[i-10],0) - 1
            
            curmap = s[i:i+10] 
            
            
            if curmap in allsets:
                if not curmap in result: 
                    result.add(curmap)
            
            allsets.add(curmap)
        
        return result
            
            
            