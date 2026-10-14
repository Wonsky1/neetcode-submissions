# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_list_1_item = list1
        current_list_2_item = list2
        resulting_list = None
        resulting_list_head = None
        while any((current_list_1_item != None, current_list_2_item != None)):
            if current_list_1_item and (current_list_2_item is None or current_list_1_item.val < current_list_2_item.val):
                smaller_val = current_list_1_item.val
                current_list_1_item = current_list_1_item.next
            else:
                smaller_val = current_list_2_item.val
                current_list_2_item = current_list_2_item.next
            if resulting_list:
                resulting_list.next = ListNode(smaller_val)
                resulting_list = resulting_list.next
            else:
                resulting_list_head = resulting_list = ListNode(smaller_val) 

        return resulting_list_head

        