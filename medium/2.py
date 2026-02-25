# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = 0, 0
        p1, p2 = 0, 0

        while l1:
            n1 += l1.val * (10 ** p1)
            p1 += 1
            l1 = l1.next

        while l2:
            n2 += l2.val * (10 ** p2)
            p2 += 1
            l2 = l2.next
        
        n3 = n1 + n2
        l3 = ListNode(n3 % 10)
        n3 //= 10
        curr = l3
        while n3 > 0:
            node = ListNode(n3 % 10)
            n3 //= 10
            curr.next = node
            curr = curr.next

        return l3
