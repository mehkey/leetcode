class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        t = len(nums)

        def binary_search(arr, low, high, x):
 
            if high >= low:

                mid = (high + low) // 2

                if arr[mid] == x:
                    return mid


                elif arr[mid] > x:
                    return binary_search(arr, low, mid - 1, x)

                else:
                    return binary_search(arr, mid + 1, high, x)

            else:
                return -1
 
        count = 0
        for i,n in enumerate(nums):
            if binary_search(nums, 0, i-1, n-diff) != -1  and binary_search(nums, i+1, t-1,n + diff) != -1:
                count+=1
        
        return count