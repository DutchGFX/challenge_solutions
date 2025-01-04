# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        """
        Returns an array of the largest value at each level of a tree

        Notes
        -----
        - We perform a BFS by pushing children to a queue and then looping over all
          child nodes
        """
        if root is None:
            return []
        children = []
        maxvals = []
        current = [root]
        while current:
            # append to maxvals
            maxvals.append(-float("inf"))

            # loop over nodes
            for node in current:
                maxvals[-1] = max(maxvals[-1], node.val)
                if node.left is not None:
                    children.append(node.left)
                if node.right is not None:
                    children.append(node.right)

            # update
            current = children
            children = []

        return maxvals
