# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #Pointing the pointers to left
        dummy = ListNode(0, head)
        
        leftPrev, curr = dummy, head
        
        for i in range(left - 1):
            leftPrev, curr = curr, curr.next
            
        #reversing the list
        prev = None
        for i in range(right - left + 1):
            currNext = curr.next
            curr.next = prev
            prev, curr = curr, currNext
            
        #Joining the list
        leftPrev.next.next = curr
        leftPrev.next = prev
        
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         lft, rite = head, head
        
#         for i in range(left):
#             if i == left - 1:
#                 leftHead = lft
#                 leftHead.next = None
#             lft = lft.next
            
#         for j in range(right):
#             rite = rite.next
#             if rite.next:
#                 rightHead = rite.next
                
#         prev, curr = rightHead, lft
        
#         while curr.next != rite:
#             currNext = curr.next
#             curr.next = prev
#             prev, curr = curr, currNext
            
#         leftHead.next = curr
        
        
#         return curr
