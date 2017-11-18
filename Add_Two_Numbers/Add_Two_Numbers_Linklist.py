# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = n = ListNode(0)
        carry = 0
        while l1 or l2 or carry:  # don't forget carry!
            if l1:
                val_1 = l1.val
                l1 = l1.next
            else:
                val_1 = 0
                
            if l2:
                val_2 = l2.val
                l2 = l2.next
            else:
                val_2 = 0
                
            val = (carry + val_1 + val_2) % 10
            carry = (carry + val_1 + val_2) // 10
            n.next = n = ListNode(val)
            
        return root.next
            
            
            
            