# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last = None
        p = None
        while head:
            p = ListNode(head.val)
            p.next = last
            last = p
            head = head.next
        return p


vals = [1,2,3,4,5]
root = ListNode(0)
p = root
for val in vals:
    p.next = ListNode(val)
    p = p.next

q = Solution().reverseList(root)

a = []
while q:
    a.append(q.val)
    q = q.next

print a
    


