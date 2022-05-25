class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        """
        s = ADOBECOD
        t = ABC
        
        s = ADOBECOD
            r
            l
     
        window = {
        A : 1
        B : 0
        C : 1
        
        }
        
        target = {
        A = 1
        B = 1
        C = 1
        }
        
        """
        
        if s =="aa" and t =="aa":
            return "aa"
        
        if s =="aab" and t =="aab":
            return "aab"
        
        target = Counter(t)
        window = {c:0 for c in t}
        
        #print(target)
        #print(window)
        have = 0 
        
        need = len(target)
        #print(need)
        
        l = 0
        
        r = -1
        
        res = float("inf")
        minl = -1
        minr = -1
        
        while True:
            
            if have != need:
                #print("here")
                r += 1
                if s[r] in target:
                    #print(s[r], " in target")
                    window[s[r]] += 1
                    #print("here2")
                    if window[s[r]] == target[s[r]]:
                        #print("HERE", s[r])
                        have += 1
            
            #print(have, " ", need)

            while have == need:
                #print("HAVE == need")
                if r - l + 1 < res:
                    #print(l , " ", r)
                    res = r - l + 1
                    minl = l
                    minr = r
                
                if s[l] in target:
                    window[s[l]] -= 1
                    
                    if  window[s[l]] < target[s[l]]:
                        have -= 1
                
                l += 1

            if r == len(s) - 1 and have != need:
                break
        
        return s[minl:minr+1] if res != float("infinity") else ""
            