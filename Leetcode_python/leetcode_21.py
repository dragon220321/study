# Merge two sorted linked lists
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        temp = ListNode(0)
        temp1 = temp
        while p and q:
            if p.val > q.val:
                temp.next = q
                q = q.next
            else:
                temp.next = p
                p = p.next
            temp = temp.next
        if p:
            temp.next = p
        else:
            temp.next = q

        return temp1.next

# test
buff = ListNode(0)
l1 = buff
for i in [1,2,4]:
    t = ListNode(i)
    buff.next = t
    buff = t
l1 = l1.next
buff = ListNode(0)
l2 = buff
for j in [1,3,4]:
    t = ListNode(j)
    buff.next = t
    buff = t
l2 = l2.next
sln = Solution()
l3 = sln.mergeTwoLists(l1,l2)
while l3 != None:
    print(l3.val)  
    l3 = l3.next     