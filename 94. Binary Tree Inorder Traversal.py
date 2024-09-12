# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive
# class Solution:
#     def inorderTraversal(self, node: TreeNode | None) -> list[int]:
#         res = []

#         def dfs(node):
#             if node:
#                 dfs(node.left)
#                 res.append(node.val)
#                 dfs(node.right)

#         dfs(node)
#         return res


# Iterative
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        if root is None:
            return res

        # curr  = 8
        # stack = []
        # res   = [4, 2, 6, 5, 7, 1, 3, 9, 8]
        # used  = {4, 2, 6, 5, 7, 1, 3, 9, 8}
        used = set()
        stack = [root]  
        while stack:
            curr = stack[-1]
            if curr.left and curr.left not in used:
                stack.append(curr.left)

            else:
                res.append(curr.val)
                stack.pop()
                used.add(curr)
                if curr.right:
                    stack.append(curr.right)



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
assert (res := sln.inorderTraversal(root)) == [4,2,6,5,7,1,3,9,8], res
