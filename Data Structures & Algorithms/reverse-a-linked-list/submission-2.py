# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
        # array = []
        # if head == None:
        #     return head
        # while head!= None:
        #     array.append(head.val)
        #     head = head.next
        # array.reverse()
        # rev = ListNode()
        # a = rev
        # for i in range(len(array)):
        #     rev.val = array[i]
        #     if i == len(array)-1:
        #         rev.val = array[i]
        #         rev.next = None
        #     else:
        #         nextnode = ListNode(0)
        #         rev.next = nextnode
        #         rev = rev.next
        # return a
