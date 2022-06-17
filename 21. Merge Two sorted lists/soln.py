class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    sol = temp = ListNode()
    while list1 and list2:
        if(list1.val>list2.val):
            temp.next = list2
            list2 = list2.next
        else:
            temp.next = list1
            list1 = list1.next
        temp = temp.next
    if list1 or list2:
        temp.next = list1 if list1 else list2
    return sol.next
    
li1 = [1,2,4]
li2 = [1,3,4]

a = ListNode()
list1 = a
for n in li1:
    a.next = ListNode(n)
    a = a.next

b = ListNode()
list2 = b
for n in li1:
    b.next = ListNode(n)
    b = b.next

mergeTwoLists(list1.next, list2.next)
