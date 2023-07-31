# 2. Add Two Numbers
### 問題
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### 翻譯
您被給予兩個非空的鏈結串列，代表兩個非負整數。這些數字以相反的順序存儲，每個節點包含一個單個數字。請將這兩個數字相加，並將結果以鏈結串列形式返回。

您可以假設這兩個數字除了數字0本身之外，不包含任何前導零。

##### Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

     2 -> 4 -> 3
     5 -> 6 -> 4
    --------------
     7 -> 0 -> 8
##### Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]
##### Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

### 想法
一開始想到的方法是直接把鏈結串列，全部轉成整數，然後相加，再轉回去，超級暴力XDDD  
可是觀察後發現，其實題目有提示，他就是一般的加法直式，從個位數十位數一直上去，只是要處理下進位問題，還有要小心 l1,比 l2 長，或是 l2 比 l1 長，導致導致沒有抓到數字變 null，ex: Example 3 。

### 解法
```python
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
```