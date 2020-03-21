# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # use two pointers

        # temp = head
        # while temp != None:
        #     print(temp.val)
        #     temp = temp.next

        #Initializing values
        dh = ListNode('dummy')
        dh.next = head

        temp = head

        for i in range(n):
            temp = temp.next
        pt2 = head

        while temp.next != None:
            temp = temp.next
            pt2 = pt2.next

        # remove the next node from pointer 2
        pt2.next = pt2.next.next

        return head
