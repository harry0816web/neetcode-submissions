# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        newRoot = None

        while cur is not None:
            nextNode = cur.next
            prev = newRoot

            newRoot = cur
            newRoot.next = prev

            cur = nextNode
        
        return newRoot


        