# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #finding middle
        initial = head
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #spliting
        newStart = slow.next
        slow.next = None
        
        #reversing the new
        prev, curr = None, newStart
        
        while curr:
            newCurr = curr.next
            curr.next = prev
            prev, curr = curr, newCurr
            
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
