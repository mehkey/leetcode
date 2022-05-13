class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        
        def compare(n1,n2):
            if str(n1) + str(n2) > str(n2) + str(n1):
                return -1
            else:
                return 1

        sortedlist = sorted(nums,key=cmp_to_key(compare))

        #print(sortedlist)
        #print("".join(map(str,sortedlist)))
        
        return str(int("".join(map(str,sortedlist))))