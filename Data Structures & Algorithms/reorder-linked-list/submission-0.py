# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list_ = []
        new = head
        while head:
            list_.append(head.val)
            head = head.next
        # print(list_)
        # left, right = 0, len(list_)
        now_real = True
        i = 0
        while new:
            if now_real:
                new.val = list_[i]
                i += 1
            else:
                new.val = list_[-i]
            new = new.next
            now_real = not now_real
        # while left < right:
