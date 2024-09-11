# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive
class Solution:
    def preorderTraversal(self, node: TreeNode | None) -> list[int]:
        res = []

        def dfs(node):
            if node:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(node)
        return res


# Iterative
# class Solution:
#     def preorderTraversal(self, root: TreeNode | None) -> list[int]:
#         res: list[int] = []
#         if root is None:
#             return res

#         vertices = [root]
#         while vertices:
#             node = vertices.pop()
#             res.append(node.val)
#             if node.right:
#                 vertices.append(node.right)
#             if node.left:
#                 vertices.append(node.left)

#         return res


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
assert sln.preorderTraversal(root) == [1, 2, 4, 5, 6, 7, 3, 8, 9]
