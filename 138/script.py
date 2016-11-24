# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        class RootNode:
            def __init__(self):
                self.next = None
        p = RootNode()
        p.next = head
        tbl = {}
        root = RootNode()
        np = root
        while p.next:
            p = p.next
            np.next = RandomListNode(p.label)
            np = np.next
            if p.label in tbl:
                for node in tbl[p.label]:
                    node.random = np
            tbl[p.label] = np

            if p.random:
                if p.random.label in tbl and isinstance(tbl[p.random.label], RandomListNode):
                    np.random = tbl[p.random.label]
                else:
                    if p.random.label not in tbl:
                        tbl[p.random.label] = []
                    tbl[p.random.label].append(np)
        return root.next
            






