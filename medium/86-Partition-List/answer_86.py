# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        before_part = ListNode(0)
        after_part = ListNode(0)

        before_current = before_part
        after_current = after_part

        while head:
            if head.val < x:
                before_current.next = head
                before_current = head
            else:
                after_current.next = head
                after_current = head
            
            head = head.next

        
        after_current.next = None
        before_current.next = after_part.next
        
        return before_part.next
