from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next
        # 當快指針等於 None 時，代表要找的值就是第一個值，直接拿掉他，回傳第二個節點
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next

        return head


#測試
solution = Solution()
aaa = ListNode(1)
print(solution.removeNthFromEnd(aaa, 1))