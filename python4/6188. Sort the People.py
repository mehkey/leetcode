class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        p = list(zip(names,heights))

        p.sort(key=lambda x: (-x[1],x[0]))


        return list(map(lambda x: x[0],p))