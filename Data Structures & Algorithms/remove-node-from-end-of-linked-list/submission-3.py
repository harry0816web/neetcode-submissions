# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count the length
        cur = head
        length = 0
        while cur is not None:
            length += 1
            cur = cur.next

        # remove node
        target_idx = length - n
        if target_idx == 0: # removing the head
            return head.next

        remove_next = head
        # 0 1 2 3, target = 3
        #     ^
        # print(target_idx)
        while target_idx > 1:
            target_idx -= 1
            remove_next = remove_next.next

        # if target_idx == length - 1: # last one
        #     if length == 1:
        #         head = None
        #     else:
        #         remove_next.next = None
        remove_next.next = remove_next.next.next

        return head