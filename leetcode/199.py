# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        view = [(root, 0)]
        queue = [(root, 0)]

        while queue:
            cur_node, cur_height = queue.pop(0)
            if cur_height == view[-1][1]:
                view.pop()
            view.append((cur_node, cur_height))

            if cur_node.left != None:
                queue.append((cur_node.left, cur_height+1))
            if cur_node.right != None:
                queue.append((cur_node.right, cur_height+1))
        return [node.val for node, _ in view]
    
# Solved 9m50s