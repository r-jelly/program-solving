# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        len_list = 1
        cur_node = head
        while cur_node.next is not None:
            cur_node = cur_node.next
            len_list += 1
        # O(N)

        if len_list==1:
            return None

        mid_idx = len_list//2
        prev_node = None
        cur_node = head
        for i in range(mid_idx):
            prev_node = cur_node
            cur_node = cur_node.next
        prev_node.next = cur_node.next
        return head