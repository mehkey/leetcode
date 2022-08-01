class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        
        grades.sort()
        
        print(grades)
        
        cur = 0
        res = 0
        
        cur_g = 0
        cur_r = 0
        prev_g = 0
        prev_r = 0
        
        for i in range(len(grades)):
            cur_g += grades[i]
            cur_r += 1
            
            if cur_g > prev_g and cur_r > prev_r:
                res = cur_r
                prev_g = cur_g 
                prev_r = cur_r 
                cur_g =0
                cur_r = 0

        return res