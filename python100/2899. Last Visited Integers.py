class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        
        ind = 0
        arr = []
        res = []
        for w in words:
            
            if w == 'prev':
                
                if arr and count < len(arr):
                    res.append(int(arr[-1-count]))
                    count+=1
                else:
                    res.append(-1)

            else:
                count = 0
                arr.append(w)
        
        return res
                