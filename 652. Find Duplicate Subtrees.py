# https://leetcode.com/problems/find-duplicate-subtrees/description/

from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:
        duplicates = []
        seen = defaultdict(int)

        def find(node):
            if node is None:
                return '#'

            left = find(node.left)
            right = find(node.right)
            h = str(node.val) + '.' + left + '.' + right + '.'

            seen[h] += 1
            if seen[h] == 2:
                duplicates.append(node)
            return h

        find(root)
        return duplicates


node31 = TreeNode(3)
node21 = TreeNode(2, node31)
node32 = TreeNode(3)
node22 = TreeNode(2, node32)
root = TreeNode(2, node21, node22)

sln = Solution()
assert sln.findDuplicateSubtrees(root) == [node32, node22]
