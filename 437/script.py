# Definition for a binary tree node.

from shared.tree import deserialize, drawtree
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        def dfs(cumsum, root):
            cumsum.append(cumsum[-1] + root.val)
            cnt = 0
            for s in cumsum[:-1]:
                print root.val, cumsum[-1] - s
                if cumsum[-1] - s == sum:
                    cnt += 1
            if root.left:
                cnt += dfs(cumsum, root.left)
            if root.right:
                cnt += dfs(cumsum, root.right)
            cumsum.pop()
            return cnt
        return dfs([0], root)


#root = deserialize('[10,5,-3,3,2,null,11,3,-2,null,1]')
root = deserialize('[5,4,8,11,null,13,4,7,2,null,null,5,1]')
#drawtree(root)
print Solution().pathSum(root, 22)

