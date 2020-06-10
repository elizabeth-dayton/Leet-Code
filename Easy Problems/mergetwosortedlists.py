# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Try 1 - ran in 28 ms and took 12.8 MB of memory

def mergeTwoLists(l1, l2):

    # :type l1: ListNode
    # :type l2: ListNode
    # :rtype: ListNode 
    mergedList = ListNode()
    iterator = mergedList

    while l1 is not None and l2 is not None:
        if l1.val >= l2.val:
            iterator.next = ListNode(l2.val)
            l2 = l2.next
        elif l1.val <= l2.val:
            iterator.next = ListNode(l1.val)
            l1 = l1.next
        iterator = iterator.next

    if l1 is None:
        while l2 is not None:
            iterator.next = ListNode(l2.val)
            l2 = l2.next
            iterator = iterator.next

    elif l2 is None:
        while l1 is not None:
            iterator.next = ListNode(l1.val)
            l1 = l1.next
            iterator = iterator.next

    return mergedList.next

#Testing
def listToNodes(num_list, index):
    try:
        return ListNode(num_list[index], listToNodes(num_list, index + 1))
    except:
        return None
 
def nodesToList(curr_node):
    node_list = []
    while curr_node != None:
        node_list.append(curr_node.val)
        curr_node = curr_node.next
    return node_list
 
llist = listToNodes([9, 9, 9], 0)
rlist = listToNodes([1], 0)

xlist = listToNodes([1, 2, 4], 0)
ylist = listToNodes([1, 3, 4], 0)

plist = listToNodes([2, 3, 4], 0)
qlist = listToNodes([4, 5, 6], 0)

alist = mergeTwoLists(llist, rlist)
blist = mergeTwoLists(xlist, ylist)
clist = mergeTwoLists(plist, qlist)

print(nodesToList(alist))
print(nodesToList(blist))
print(nodesToList(clist))  