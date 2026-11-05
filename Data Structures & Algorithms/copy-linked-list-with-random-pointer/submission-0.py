"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # class RandomNode:
        #     def __init__(self, next: 'Node' = None, random: 'Node' = None):
        #         self.next = next
        #         self.random = random

        # random_head = RandomNode(head.next, head.random)
        random_list = {}
        def deep_copy(node) -> Node:
            if node is None:
                return None
            else: 
                new_node = Node(node.val, deep_copy(node.next), None)
                random_list[node] = new_node
                return new_node

        new_head = deep_copy(head)

        # copy random
        cur = head
        new_cur = new_head
        while cur is not None:
            if cur.random is None:
                new_cur.random = None
            else:
                new_cur.random = random_list[cur.random]
            cur = cur.next
            new_cur = new_cur.next

        
        return new_head
        
        