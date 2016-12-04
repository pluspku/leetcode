# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import random
        node = self.head
        pnode = None
        rmax = -1
        while node:
            r = random.random()
            if r > rmax:
                pnode = node
                rmax = r
            node = node.next
        return pnode.val

        


# Your Solution object will be instantiated and called as such:

head = ListNode(1);
head.next = ListNode(2);
head.next.next = ListNode(3);

obj = Solution(head)
param_1 = obj.getRandom()
print param_1

