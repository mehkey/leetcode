class Solution:
    def countDigits(self, num: int) -> int:
        str_num = str(num)
        
        count = 0
        
        for c in str_num:
            if num % int(c) == 0:
                count+=1
        
        return count