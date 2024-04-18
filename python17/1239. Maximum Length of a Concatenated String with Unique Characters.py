class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        arr.sort()
        
        N = len(arr)
        
        @cache
        def dp(i, bit_map, tot):
            if i == N:
                return tot 
        
            new_map = 0
            res = 0
            
            for c in arr[i]:
                if new_map &  ( 1 <<  ( ord(c) - ord('a') ) ):

                    return  dp(i+1, bit_map, tot)  

                new_map |=  ( 1 <<  ( ord(c) - ord('a') ) )
            
            if bit_map & new_map :

                res = max(  dp(i+1, bit_map, tot) , dp(i+1, new_map, len(arr[i])  )   )

            else:

                res =  max( dp(i+1, bit_map | new_map, tot +  len(arr[i]) )  , dp(i+1, bit_map , tot )  , dp(i+1, new_map, len(arr[i]) )   )
            
            return res

        return dp(0,0,0 )