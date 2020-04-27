# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    # use two pointers; one is always n steps ahead of the other
    # when pt1 is at the end of the linked list, pt2 is on the node right before
    # the nth Node
    # adjust pt2.next = pt2.next.next

    # temp = head
    # while temp != None:
    #     print(temp.val)
    #     temp = temp.next

    #Initializing values
    dh = ListNode('dummy')
    dh.next = head

    temp = head

    # walk temp n steps ahead
    for i in range(n):
        temp = temp.next
    pt2 = head

    while temp.next != None:
        temp = temp.next
        pt2 = pt2.next

    # remove the next node from pointer 2
    pt2.next = pt2.next.next

    return head
