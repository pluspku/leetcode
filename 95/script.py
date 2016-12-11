import asciitree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def listify(self):
        ll = self.left.listify() if self.left else []
        rr = self.right.listify() if self.right else []
        return [(val, d + 1) for val, d in ll] + [(self.val, 0)] + [(val, d+1) for val, d in rr]

    def __str__(self):
        ret = ''
        for val, d in self.listify():
            ret += '%s%s\n' % (' ' * d, val)
        return ret
    __repr__ = __str__

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        res = []
        dat = {}
        def search(l, r):
            if (l, r) in dat:
                return dat[(l, r)]
            if l > r:
                return [None]
            if l == r:
                return [TreeNode(l)]
            ret = []
            for i in xrange(l, r+1):
                lc = search(l, i - 1)
                rc = search(i + 1, r)
                for a in lc:
                    for b in rc:
                        root = TreeNode(i)
                        root.left = a
                        root.right = b
                        ret.append(root)
            return ret

        return search(1, n) if n > 0 else []

for tree in Solution().generateTrees(1):
    print tree
    print
