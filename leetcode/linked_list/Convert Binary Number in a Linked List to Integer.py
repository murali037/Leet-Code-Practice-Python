class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        bitstring = ""

        while cur:
            bitstring += str(cur.val)
            cur = cur.next
        return int(bitstring, 2)
