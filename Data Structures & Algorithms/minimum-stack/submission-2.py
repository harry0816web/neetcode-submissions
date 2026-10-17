class MinStack:
    class Node:
        def __init__(self, val, min_val, next=None):
            self.val = val
            self.next = next   # points to the next Node, or None   

            # O(1) getMin() tarverse when insert
            self.min_val = min_val

    def __init__(self):
        self.root = None

    def push(self, val: int) -> None:
        # O(1) getMin()
        min_val = val
        if self.root != None:
            min_val = min(val, self.root.min_val)

        self.root = self.Node(val, min_val, self.root)

    def getTop(self) -> int:
        return self.root.val

    def pop(self) -> None:
        """
        Python frees memory on its own: every object keeps a count 
        of how many variables point to it, and when that count drops 
        to 0, the object is deleted right away.
        """
        self.root = self.root.next

    def top(self) -> int:
        return self.getTop()

    def getMin(self) -> int:
        # min_val = self.getTop()
        # cur = self.root

        # while cur != None:
        #     min_val = min(cur.val, min_val)
        #     cur = cur.next

        return self.root.min_val


        
