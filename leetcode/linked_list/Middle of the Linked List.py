# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node = head

        L = []
        while node:
            L.append(node.val)
            node = node.next

        if len(L) == 1 or len(L) == 0:
            return head
        elif len(L) == 2:
            head = head.next
            return head

        if len(L) % 2 == 0:
            middle_element = int(len(L) / 2 + 1)
        else:
            middle_element = int(len(L) // 2 + (len(L) % 2 > 0))

        x = L[middle_element - 1]
        next_elem = L[middle_element]
        print(len(L), middle_element, x, next_elem)

        node = head

        while True:
            node = node.next
            if node.val == x and node.next.val == next_elem:
                print(node.val, node.next.val)
                break
        return node


#%% short and fast solution

A = [head]
while A[-1].next:
    A.append(A[-1].next)
return A[int(len(A) / 2)]


#%% fast and slow pointer

slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow
