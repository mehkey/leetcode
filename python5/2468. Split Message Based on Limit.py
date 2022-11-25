class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        
        
        def buildnum(start,total):
            
            return f'<{start}/{total}>'
            
        output = []
        
        if limit-5 <= 0:
            return []
        else:
            total = ceil(len(message) / (limit-3-2))
        
        total = '&'* len(str(total))
        
        buff = []

        count = 1
        
        for i,c in enumerate(message):

            buff.append(c)

            if len(buff) + len(buildnum(count,total)) == limit:

                output.append( ''.join(buff) + buildnum(count,total) )    
                buff = []
                count += 1
            elif len(buff) + len(buildnum(count,total)) > limit :
                return []
                
        if len(buff) > 0:
            output.append( ''.join(buff) + buildnum(count,total) )    
            count += 1
        
        count -= 1
        output = [s.replace(total,str(count)) for s in output]
        return output

        