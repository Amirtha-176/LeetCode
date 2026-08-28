class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        ref = dummy
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                ref.next = cur.next
            else:
                ref = ref.next
            cur = cur.next

        return dummy.next