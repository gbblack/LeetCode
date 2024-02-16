# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sol1 = []
        sol2 = []

        while l1:
            sol1.append(l1.val)
            l1 = l1.next
        
        while l2:
            sol2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        root = None
        
        while sol1 or sol2 or carry:
            val1 = 0
            val2 = 0

            if sol1:
                val1 = sol1.pop()
            if sol2:
                val2 = sol2.pop()
            
            carry, total_value = divmod(val1+val2+carry, 10)

            res = ListNode(total_value)
            res.next = root
            root = res

        return root