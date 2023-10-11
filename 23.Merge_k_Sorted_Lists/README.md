# 23. Merge k Sorted Lists
### 問題
You are given an array of **k** linked-lists **lists**, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
 ### 翻譯
你被給予一個包含 **k** 個鏈結串列的陣列 **lists**，每個鏈結串列都按升序排序。

將所有的鏈結串列合併成一個按升序排序的鏈結串列，然後返回它。
##### Example 1:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
    1->4->5,
    1->3->4,
    2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6
##### Example 2:
    Input: lists = []
    Output: []
##### Example 3:
    Input: lists = [[]]
    Output: []

##### Constraints:
- k == lists.length
- 0 <= k <= 10<sup>4</sup>
- 0 <= lists[i].length <= 500
- -10<sup>4</sup> <= lists[i][j] <= 10<sup>4</sup>
- lists[i] is sorted in **ascending order**.
- The sum of lists[i].length will not exceed 10<sup>4</sup>

### 想法 1
這題最簡易的解法就是利用之前 [21. Merge Two Sorted Lists](https://github.com/Chechih/LeetCode_Py/tree/master/21.Merge_Two_Sorted_Lists) 的 Function 下去延伸，將**鏈結串列**兩兩下去合併，Ex: A1 和 A2 合併成 B1， A3 和 A4 合併成 B2， A5 和 A6 合併成 B3... B1 和 B2 合併成 C1 ... 這樣下去合併。其實也可以 B1 和 A3 合併，在和 A4 一直合併下去，只是這樣主要的**鏈結串列**會越來越長，導致效能不好。
### 解法 1
```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        newList = ListNode()
        rlt = newList
        previous = newList # 清除掉最後面多餘的節點用的
        while list1 or list2:
            if list1 and (not list2 or list1.val <= list2.val):
                newList.val = list1.val
                list1 = list1.next
            else:
                newList.val = list2.val
                list2 = list2.next
            previous = newList
            newList.next = ListNode()
            newList = newList.next
        if previous:
            previous.next = None

        return rlt
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        left = 0
        right = len(lists) - 1
        while len(lists) > 1:
            if left < right:
                lists[left] = self.mergeTwoLists(lists[left], lists[right])
                lists.remove(lists[right])
                left += 1
                right -= 1
            else:
                left = 0
                right = len(lists) - 1
        return lists[0] if len(lists) > 0 else None 
```
### 想法 2
網路上參考其他人作法時，有些人是使用**優先佇列(Priority Queue)**的做法，這東西可以自動排序裡面存在的值，所以你可以把所有的**鏈結串列**讀出，塞到**優先佇列(Priority Queue)**裡面，然後，再把所有的**優先佇列(Priority Queue)**讀出，建一個新的**鏈結串列**即是題目要求的東西了。
### 解法 2
```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = queue.PriorityQueue()
        for i in range(len(lists)):
            l = lists[i]
            while(l != None):
                q.put(l.val)
                l = l.next
        if q.empty():
            return None
        rlt = ListNode()
        rlt.val = q.get()
        rlt.next = None
    
        new_node = rlt
        while not q.empty():
            new_node.next = ListNode()
            new_node = new_node.next
            new_node.val = q.get()
            new_node.next = None
        
        return rlt
```
### 想法 3
你一定想說**優先佇列(Priority Queue)**都可以了，那我直接用個 Array 存**鏈結串列**所有的值，在 Sort(排序)，再轉出新的**鏈結串列**，應該也可以，我去時做的發現也可以過XDDD
### 解法 3
```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_vals = []
        for i in range(len(lists)):
            l = lists[i]
            while(l != None):
                all_vals.append(l.val)
                l = l.next
        if len(all_vals) == 0:
            return None
        all_vals.sort()
        all_vals.reverse()
        rlt = ListNode()
        rlt.val = all_vals.pop()
        rlt.next = None
    
        new_node = rlt
        while len(all_vals) > 0:
            new_node.next = ListNode()
            new_node = new_node.next
            new_node.val = all_vals.pop()
            new_node.next = None
        
        return rlt
```
