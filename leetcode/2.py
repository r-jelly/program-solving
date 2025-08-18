# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node_list = []
        add_cnt = 0
        while l1 != None or l2 != None:
            cur_val = add_cnt
            if l1 != None: cur_val += l1.val
            if l2 != None: cur_val += l2.val
            
            if cur_val >= 10:
                add_cnt = 1
                cur_val -= 10
            else:
                add_cnt = 0
            newNode = ListNode(cur_val)
            node_list.append(newNode)
            
            if l1 != None: l1 = l1.next
            if l2 != None: l2 = l2.next
        if add_cnt == 1:
            node_list.append(ListNode(1))

        for i in range(len(node_list)-1):
            node_list[i].next = node_list[i+1]
        return node_list[0]
    
# Solved 26m30s