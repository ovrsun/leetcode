# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, node: TreeNode | None) -> int:
        if node is None:
            return 0
        left_depth = self.maxDepth(node.left)
        right_depth = self.maxDepth(node.right)
        return max(left_depth, right_depth) + 1


node9 = TreeNode(9)
node15 = TreeNode(15)
node7 = TreeNode(7)
node20 = TreeNode(20, node15, node7)
node3 = TreeNode(3, node9, node20)

sln = Solution()
assert (res := sln.maxDepth(node3)) == 3, res
assert (res := sln.maxDepth(None)) == 0, res
