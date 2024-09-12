# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive
# class Solution:
#     def postorderTraversal(self, root: TreeNode | None) -> list[int]:
#         if root is None:
#             return []
        
#         res = []

#         def dfs(node):
#             if node:
#                 dfs(node.left)
#                 dfs(node.right)
#                 res.append(node.val)

#         dfs(root)
#         return res


# Iterative
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        res = []
        stack = [root]
        used = set()

        while stack:
            curr = stack[-1]
            if curr.left and curr.left not in used:
                stack.append(curr.left)
                used.add(curr.left)
                continue

            if curr.right and curr.right not in used:
                stack.append(curr.right)
                used.add(curr.right)
                continue
            
            res.append(curr.val)
            stack.pop()
        
        return res



node4 = TreeNode(4)
node6 = TreeNode(6)
node7 = TreeNode(7)
node5 = TreeNode(5, node6, node7)
node2 = TreeNode(2, node4, node5)
node9 = TreeNode(9)
node8 = TreeNode(8, left=node9)
node3 = TreeNode(3, right=node8)
root = TreeNode(1, node2, node3)

sln = Solution()
assert sln.postorderTraversal(root) == [4, 6, 7, 5, 2, 9, 8, 3, 1]
