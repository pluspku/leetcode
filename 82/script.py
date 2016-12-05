# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '%s->%s' % (self.val, self.next)

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        last = ListNode(None)
        root = ListNode(None)
        q = root
        stage = None
        while p:
            if p.val == last.val:
                stage = None
            elif stage is None:
                stage = p
            elif stage.val != p.val:
                q.next = ListNode(stage.val)
                q = q.next
                stage = p
            last = p
            p = p.next
        if stage:
            q.next = ListNode(stage.val)
        return root.next


inputs = [1,1,2,3,4,4,5,6,6,7,8]
r = ListNode(None)
p = r
for x in inputs:
    p.next = ListNode(x)
    p = p.next

print Solution().deleteDuplicates(r.next)
