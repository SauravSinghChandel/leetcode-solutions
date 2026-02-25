# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head

        while curr:

            while curr and prev.val == curr.val:
                curr = curr.next

            prev.next = curr
            if curr:
                prev, curr = curr, curr.next

        return head
