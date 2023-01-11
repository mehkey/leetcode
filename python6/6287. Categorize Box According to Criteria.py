class Solution:
    def categorizeBox(self, l: int, w: int, h: int, m: int) -> str:
        f = 10**4
        ff = 10**9
        
        v = l*w*h
        
        b = False
        
        if l >= f or w >= f or h >= f or v >= ff:
            b = True
        
        hv = False
        
        if m >= 100:
            hv = True
        
        if b and hv:
            return "Both"
        
        if not b and not hv:
            return "Neither"
        
        if b and not hv:
            return "Bulky"
        
        if hv and not b:
            return "Heavy"
        