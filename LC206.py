# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            prev = {}
            point = head
            while point.next is not None:
                prev[point.next] = point
                point = point.next
            
            new_head = point

            while point != head:
                point.next = prev[point]
                point = prev[point]
            
            point.next = None
            head = new_head

        return head
