# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    
    # :type l1: ListNode
    # :type l2: ListNode
    # :rtype: ListNode

# Try 1 - ran in 60 ms and took 12.7 MB of memory
    carry = 0
    root = ListNode()
    num = root

    while l1 is not None and l2 is not None:
        sum = l1.val + l2.val + carry
        carry = 0
        if sum > 9:
            if sum == 10:
                carry = sum // 10
                sum = 0
            else:
                carry = sum // 10
                sum = sum - 10
        l1 = l1.next
        l2 = l2.next
        num.next = ListNode(sum)
        num = num.next

    while l1 is not None:
        sum = carry + l1.val
        carry = 0
        if sum > 9:
            carry = sum / 10
            sum = 0
        num.next = ListNode(sum)
        num = num.next
        l1 = l1.next

    while l2 is not None:
        sum = carry + l2.val
        carry = 0
        if sum > 9:
            carry = sum / 10
            sum = 0
        num.next = ListNode(sum)
        num = num.next
        l2 = l2.next

    if carry > 0:
        num.next = ListNode(carry)

    return root.next

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

xlist = listToNodes([0, 1], 0)
ylist = listToNodes([], 0)

plist = listToNodes([2, 4, 3], 0)
qlist = listToNodes([5, 6, 4], 0)

alist = addTwoNumbers(llist, rlist)
blist = addTwoNumbers(xlist, ylist)
clist = addTwoNumbers(plist, qlist)

print(nodesToList(alist))
print(nodesToList(blist))
print(nodesToList(clist))