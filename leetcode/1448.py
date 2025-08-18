# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [(root, root.val)]
        cnt = 0
        while stack:
            cur_node, cur_path_max = stack.pop()
            if cur_node == None:
                continue

            if cur_node.val >= cur_path_max:
                cur_path_max = cur_node.val
                cnt += 1

            stack.extend([(cur_node.right, cur_path_max), (cur_node.left, cur_path_max)])
        return cnt
        
# Solved 27m33s