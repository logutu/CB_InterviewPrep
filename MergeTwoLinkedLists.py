def mergeTwoLl(h1, h2):
    # make two pointers to go through each list; initiate them at the heads
    # construct a head for the merged list and a walker pointer for the merged
    # linked list
    # compare the values in each list to merge the lists
    # stop when either pointer is at None ie end of the linked list then append
    # remaining portion of the other list to the merged ll

    p1 = h1
    p2 = h2

    if p1.val < p2.val:
        head = p1
        p1 = p1.next
    else:
        head = p2
        p2 = p2.next
    walker = head

    # use and for the comparison because we want it to stop as soon as either
    # pointer is at None
    while p1 != None and p2 != None:
        if p1.val < p2.val:
            walker.next = p1
            p1 = p1.next
        else:
            walker.next = p2
            p2 = p2.next
        walker = walker.next

    if p1 != None:
        walker.next = p1
    elif p2 != None:
        walker.next = p2

    return head

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

h1 = Node(1)
h1.next = Node(1)
h1.next.next = Node(3)
h1.next.next.next = Node(7)

h2 = Node(2)
h2.next = Node(5)
h2.next.next = Node(7)
h2.next.next.next = Node(8)

head = mergeTwoLl(h1, h2)

while head != None:
    print(head.val)
    head = head.next
