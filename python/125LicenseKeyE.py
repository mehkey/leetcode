class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        
        """
        
        SPLIT
        JOIN
        upper
        
        5F3Z2E9W
        
        SPECIAL case if len(chars)% k ==0
        len(chars)%k != 0
        manual split every k character
        
        runtime O(n) space(n)
        
        """
        
        
        chars = ''.join(s.split('-')).upper()
        

        if k >= len(chars):
            return chars
        
        res = ""
        
        while chars:
            res = chars[-k:] + '-'+ res
            chars = chars[:-k]

        return res[:-1]
        