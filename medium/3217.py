# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        prev = None
        curr = head

        while curr:
            if curr.val in nums:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
            else:
                prev = curr

            curr = curr.next
            
        return head
