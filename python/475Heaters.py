475. Heaters
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        heaters=[float('-inf')]+heaters+[float('inf')] # add 2 fake heaters

        ans,i = 0,0
        
        for house in houses:
            while house > heaters[i+1]:  # search to put house between heaters
                i +=1
            dis = min (house - heaters[i], heaters[i+1]- house)
            ans = max(ans, dis)

        return ans

        