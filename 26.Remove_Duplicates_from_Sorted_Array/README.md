# 26. Remove Duplicates from Sorted Array
### 問題
Given an integer array **nums** sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**. Then return the number of unique elements in **nums**.

Consider the number of unique elements of **nums** to be **k**, to get accepted, you need to do the following things:

- Change the array **nums** such that the first **k** elements of **nums** contain the unique elements in the order they were present in **nums** initially. The remaining elements of **nums** are not important as well as the size of **nums**.
- Return **k**.

**Custom Judge:**

The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }
If all assertions pass, then your solution will be **accepted**.

 ### 翻譯
給定一個以**非遞減順序**排列的整數陣列 **nums**，請**原地**移除重複的元素，以便每個獨特元素僅出現**一次**。元素的**相對順序**應該保持**不變**。然後返回陣列 **nums** 中獨特元素的數量。

考慮 **nums** 中的獨特元素數量為 **k**，為了使您的解答被接受，您需要執行以下操作：

- 修改陣列 **nums**，使得 **nums** 的前 **k** 個元素包含獨特元素，這些元素的順序與 **nums** 初始時的出現順序相同。**nums** 的其餘元素和陣列大小都不重要。
- 返回 **k**。
**自定義判定:**

判定程式將使用以下程式碼來測試您的解答：

    int[] nums = [...]; // 輸入陣列
    int[] expectedNums = [...]; // 正確長度的預期答案

    int k = removeDuplicates(nums); // 呼叫您的實作

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }

如果所有斷言都通過，則您的解答將被**接受**。
##### Example 1:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
##### Example 2:
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

##### Constraints:
- 1 <= nums.length <= 3 * 10<sup>4</sup>
- -100 <= nums[i] <= 100
- **nums** is sorted in **non-decreasing** order.

### 想法 1
這題最簡單暴力的方法就是用 **集合 (Set)**，不能重複的特性來解，也就是將題目給的 **nums** 陣列，轉成 **集合 (Set)**，再轉回 **List**，排序下，然後將原本的 **nums** 清空，將新的陣列的值全部塞回去(因為題目會驗證陣列是否正確)，即可解答。
### 解法 1
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newNums = sorted(list(set(nums)))#留下不重複的並排序
        del nums[:] #清除所有元素
        nums += newNums #合併兩個 array

        return len(newNums)
```
### 想法 2
不過我們是來練習的，不可以這麼懶(?)，所以就有了方法二的誕生，用雙指標解，
1. 指標 i 用來紀錄，要被更換的位子
2. 指針 j 用來檢查不重複的數字，然後 j 必須跑遍陣列，
3. 如果 j 找到，就和 i 互換值，並將 i 往前一位
4. 直到 j 跑完，就可以把 i 回傳(不重複的數字數量)回傳
5. 不必理會那些被換得值，題目不會去檢查
### 解法 2
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(len(nums)):
            if(nums[j] > nums[i - 1]):
                # nums[i - 1]  上一次出現的值
                # 如果比上一次出現的值大
                nums[i], nums[j] = nums[j], nums[i]
                # 互換陣列中兩個值
                i += 1
        return i
```