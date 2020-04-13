#%%

vals = []
current_node = head
while current_node is not None:
    vals.append(current_node.val)
    current_node = current_node.next
return vals == vals[::-1]


#%%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        L = []
        while head:
            L.append(head.val)
            head = head.next

        print(L)
        l, r = 0, len(L) - 1

        if len(L) == 0 or len(L) == 1:
            return True

        while True:
            print(l, r, L[l], L[r])
            if L[l] == L[r]:
                if abs(r - l) == 1:
                    print(abs(r - l))
                    break
                l += 1
                if abs(r - l) == 1:
                    print(abs(r - l))
                    break
                r -= 1
                continue
            else:
                return False

        return True

