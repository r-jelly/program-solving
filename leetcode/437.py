# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0
        stack = [(root, [0])]
        cnt = 0
        while stack:
            cur_node, cur_prefix_sum = stack.pop()
            cur_prefix_sum = cur_prefix_sum + [(cur_prefix_sum[-1] + cur_node.val)]
            for prefix_sum in cur_prefix_sum[:-1]:
                if (cur_prefix_sum[-1] - prefix_sum) == targetSum:
                    cnt += 1
            
            if cur_node.right != None:
                stack.append((cur_node.right, cur_prefix_sum))
            if cur_node.left != None:
                stack.append((cur_node.left, cur_prefix_sum))
        return cnt

# Solved 20m03s