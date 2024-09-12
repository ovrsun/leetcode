# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        q = [(root, 0)]
        levels = defaultdict(list)
        while q:
            curr, lvl = q.pop(0)
            levels[lvl].append(curr.val)
            if curr.left:
                q.append((curr.left, lvl+1))
            if curr.right:
                q.append((curr.right, lvl+1))

        res = []
        for i in range(lvl+1):
            res.append(levels[i])

        return res


node15 = TreeNode(15)
node7 = TreeNode(7)
node20 = TreeNode(20, node15, node7)
node9 = TreeNode(9)
node3 = TreeNode(3, node9, node20)

sln = Solution()
assert (res := sln.levelOrder(node3)) == [[3], [9, 20], [15, 7]], res
