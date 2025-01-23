# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        cur = root

        while cur:
            if p.val <= cur.val <= q.val or q.val <= cur.val <= p.val:
                return cur
            elif p.val <= cur.val and q.val <= cur.val:
                cur = cur.left
            else:
                cur = cur.right