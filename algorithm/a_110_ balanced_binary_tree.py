class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_balanced(self, root: TreeNode) -> bool:
        return self.depth(root) != -1

    def depth(self, node: TreeNode) -> int:
        if not node:
            return 0
        else:
            left_depth = self.depth(node.left)
            right_depth = self.depth(node.right)
            if -1 == left_depth or -1 == right_depth or abs(left_depth - right_depth) > 1:
                return -1
            else:
                return max(left_depth, right_depth) + 1
