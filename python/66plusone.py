class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        """
        res =  [int(n) for n in str(int(''.join(str(digit) for digit in digits)) + 1 ) ]

        intnumber += 1
        
        strnumber = str(intnumber)

        return [int(n) for n in strnumber]
        """

        return [int(n) for n in str(int(''.join(str(digit) for digit in digits)) + 1 ) ]