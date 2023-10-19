# 27. Remove Element
### 問題
Given an integer array **nums** and an integer **val**, remove all occurrences of **val** in **nums in-place**. The order of the elements may be changed. Then return the number of elements in **nums** which are not equal to **val**.

Consider the number of elements in **nums** which are not equal to **val** be **k**, to get accepted, you need to do the following things:

- Change the array **nums** such that the first **k** elements of **nums** contain the elements which are not equal to **val**. The remaining elements of **nums** are not important as well as the size of **nums**.
- Return **k**.
**Custom Judge:**

The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int val = ...; // Value to remove
    int[] expectedNums = [...]; // The expected answer with correct length.
                                // It is sorted with no values equaling val.

    int k = removeElement(nums, val); // Calls your implementation

    assert k == expectedNums.length;
    sort(nums, 0, k); // Sort the first k elements of nums
    for (int i = 0; i < actualLength; i++) {
        assert nums[i] == expectedNums[i];
    }
If all assertions pass, then your solution will be **accepted**.

### 翻譯
給定一個整數陣列 **nums** 和一個整數 **val**，請原地移除陣列 **nums** 中所有等於 **val** 的元素。元素的順序可能會改變。然後返回陣列 **nums** 中不等於 **val** 的元素的數量。

考慮到陣列 **nums** 中不等於 **val** 的元素數量為 **k**，為了使您的解答被接受，您需要執行以下操作：

- 修改陣列 **nums**，使得 **nums** 的前 **k** 個元素包含不等於 **val** 的元素。**nums** 的其餘元素和陣列大小都不重要。
- 返回 **k**。
**自定義判定:**

判定程式將使用以下程式碼來測試您的解答：
    int[] nums = [...]; // 輸入陣列
    int val = ...; // 要移除的數值
    int[] expectedNums = [...]; // 正確長度的預期答案。
                                // 它是排序過的，沒有值等於 val。

    int k = removeElement(nums, val); // 呼叫您的實作

    assert k == expectedNums.length;
    sort(nums, 0, k); // 對 nums 的前 k 個元素進行排序
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }
如果所有斷言都通過，則您的解答將被**接受**。

##### Example 1:
    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2,_,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 2.
    It does not matter what you leave beyond the returned k (hence they are underscores).
##### Example 2:
    Input: nums = [0,1,2,2,3,0,4,2], val = 2
    Output: 5, nums = [0,1,4,0,3,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
    Note that the five elements can be returned in any order.
    It does not matter what you leave beyond the returned k (hence they are underscores).

##### Constraints:
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100

### 想法
這題可以使用一個從尾部掃到頭的迴圈，去檢查陣列(nums)所有的值，是不是等於 val，如果是，就將他 pop 出去，因為他是從尾部開始掃的，就算他被 pop 出去，也不會有溢位的問題存在。
### 解法
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums) -1, -1, -1):#因為正循環移除會破壞迴圈的數目
            if(nums[i] == val):
                nums.pop(i)
        return len(nums)
```