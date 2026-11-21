# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_element = head
        # head.next = None
        prev_element = None
        next_element = None
        while current_element != None:
            next_element = current_element.next # pointer to 2
            current_element.next = prev_element
            prev_element = current_element
            current_element = next_element

        return prev_element