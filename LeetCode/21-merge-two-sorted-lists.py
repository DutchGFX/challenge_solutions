# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head, tail = None, None
        while list1 or list2:
            # figure out the next element
            if (not list2) or (list1 and list1.val < list2.val):
                nxt = list1
                list1 = list1.next
            else:
                nxt = list2
                list2 = list2.next

            # start the list if first iteration
            if head is None:
                head = nxt
                tail = head
            else:  # update tail
                tail.next = nxt
                tail = nxt

        return head
