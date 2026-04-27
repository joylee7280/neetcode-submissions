# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return 
        elif list1==None:
            return list2
        elif list2==None:
            return list1
        dummy = ListNode(0)
        point = dummy
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                point.next = list1
                list1 = list1.next
                point = point.next
            elif list1.val > list2.val:
                point.next = list2
                list2 = list2.next
                point = point.next
        point.next = list1 if list1 else list2
        return dummy.next


