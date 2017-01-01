# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from shared.tree import *

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        class stat:
            last = None
            first = None

        def sub(node):
            if node.left and sub(node.left):
                return True
            if stat.last:
                if node.val < stat.last.val:
                    if stat.first:
                        val = stat.first.val
                        stat.first.val = node.val
                        node.val = val
                        return True
                    else:
                        stat.first = stat.last
                elif stat.first and node.val > stat.first.val:
                    val = stat.first.val
                    stat.first.val = stat.last.val
                    stat.last.val = val
                    return True

            stat.last = node
            if node.right and sub(node.right):
                return True

        if not sub(root):
            val = stat.first.val
            stat.first.val = stat.last.val
            stat.last.val = val


tree = deserialize('[1,2,3]')
drawtree(tree)
Solution().recoverTree(tree)
drawtree(tree)
