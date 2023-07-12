from segment_tree import SegmentTree

class NumArray:

    def __init__(self, nums: List[int]):
        self.s = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.s.update(index,val)

    def sumRange(self, left: int, right: int) -> int:
        return self.s.query(left,right,"sum")


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)