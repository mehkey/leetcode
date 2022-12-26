class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        def int_to_binary(integer, i):
            binary_string = ''
            while(integer > 0):
                digit = integer % i
                binary_string += str(digit)
                integer = integer // i
            binary_string = binary_string[::-1]
            return binary_string
    
        for i in range(2, n - 1):
            
            s = ''
            k = n
            
            b = int_to_binary(k, i)
            
            if b != b[::-1]:
                return False
        
        return True
        
        
        