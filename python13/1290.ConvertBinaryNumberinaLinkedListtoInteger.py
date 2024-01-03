# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        
        cur = head
        
        while cur:
            res <<= 1 
            res ^= cur.val
            cur = cur.next
        #print(bin(res)[2:])
        return res