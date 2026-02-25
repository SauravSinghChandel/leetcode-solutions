# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        curr_fast = head

        while curr_fast and curr_fast.next:

            curr = curr.next

            curr_fast = curr_fast.next.next


        return curr
