#%%

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        def merge_linked_list(head, l1, l2):

            if l1.next or l2.next:

                if l1.val <= l2.val and l1.next:
                    head.next = l1
                    l1 = l1.next
                    merge_linked_list(head.next, l1, l2)

                elif l2.next:
                    head.next = l2
                    l2 = l2.next
                    merge_linked_list(head.next, l1, l2)
            A = [head]
            B = [head.val]
            while A[-1].next:
                A.append(A[-1].next)
                B.append(A[-1].val)
            print(B)
            return B

        while True:
            if l2.val <= l1.val:
                head = l2
                l2 = l2.next
            else:
                head = l1
                l1 = l1.next
            break

        merge_linked_list(head, l1, l2)


#%%

