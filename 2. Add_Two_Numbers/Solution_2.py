from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0#進位
        rlt = l1#回傳根節點
        #以 l1 為主要回傳的鍊錶, 將 l2 加上去
        while l2 or carry > 0:
            l1.val += carry
            if l2:
                l1.val += l2.val
                l2 = l2.next
            carry = l1.val //10#取商
            l1.val = l1.val % 10#取餘數
            if (l2 or carry > 0) and not l1.next:
                l1.next = ListNode()
            l1 = l1.next
        return rlt

solution = Solution()
#print( solution.addTwoNumbers(ListNode(9, ListNode(4, ListNode(2))), ListNode(9, ListNode(4, ListNode(6, ListNode(5))))))
print( solution.addTwoNumbers(ListNode(9, ListNode(9, ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))