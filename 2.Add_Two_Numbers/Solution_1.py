from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        isRun = True
        rlt = node = ListNode()
        carry = 0#進位
        while isRun:
            node.val = carry
            if l1:
                node.val += l1.val#加上 l1 值
                l1 = l1.next#指向下一個數字
            if l2:
                node.val += l2.val#加上 l2 值
                l2 = l2.next
            carry = node.val //10#取商
            node.val = node.val % 10
            if l1 or l2:
                node.next = ListNode()#只要還有數字, 建立新結點來存
                node = node.next
            else:
                isRun = False
        if carry > 0:#檢查是否還有進位
            node.next = ListNode(carry)
        return rlt

solution = Solution()
print( solution.addTwoNumbers(ListNode(9, ListNode(4, ListNode(2))), ListNode(9, ListNode(4, ListNode(6, ListNode(5))))))