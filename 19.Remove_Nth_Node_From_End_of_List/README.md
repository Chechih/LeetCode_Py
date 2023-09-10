# 19. Remove Nth Node From End of List
### 問題
Given the **head** of a linked list, remove the **n<sup>th</sup>** node from the end of the list and return its head.
 ### 翻譯
給定一個鏈結串列的**頭部**，刪除該串列倒數**第 n 個**節點，並返回新的串列頭部。
##### Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
![19. Remove Nth Node From End of List Example 1](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg "19. Remove Nth Node From End of List Example 1")  
圖片來源: [LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)  
##### Example 2:
    Input: head = [1], n = 1
    Output: []
##### Example 3:
    Input: head = [1,2], n = 1
    Output: [1]

##### Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

### 想法 1
這題可以用物件的特性，記憶體共用，然後把全部鏈結串列跑過一輪，存在 Array 裡面，這樣就知道個數了，然後把目標前一個 ListNode 的 next，替換調就可以了，不過要考慮一下第一個節點的狀況，和最後一個節點的狀況。
### 解法 1
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        all_nodes = []
        node = head
        while node:
            all_nodes.append(node)
            node = node.next

        target = len(all_nodes) - n
        rlt = head
        if(target == 0):# 如果沒有前一個節點
            rlt = all_nodes[0].next
        elif(target != len(all_nodes) -1):
            all_nodes[target - 1].next = all_nodes[target + 1]
        else: # 如果是最後的節點，清掉
            all_nodes[target - 1].next = None
        return rlt
```

### 想法 2
這題看了其他人的解法，還可以使用快慢指標的方法，也就是準備兩個指標，塊指標先跑 n，然後慢指標在開始跑，然後在快指標跑完時，慢指標就在目標位子上，然後在換掉 next 就可以了。
### 解法 2
```python
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
```