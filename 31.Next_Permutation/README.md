# 31. Next Permutation
### 問題
A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.

- For example, for **arr = [1,2,3]**, the following are all the permutations of **arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]**.
The **next permutation** of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the **next permutation** of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

- For example, the next permutation of **arr = [1,2,3]** is **[1,3,2]**.
- Similarly, the next permutation of **arr = [2,3,1]** is **[3,1,2]**.
- While the next permutation of **arr = [3,2,1]** is **[1,2,3]** because **[3,2,1]** does not have a lexicographical larger rearrangement.
Given an array of integers **nums**, find the next permutation of **nums**.

The replacement must be **in place** and use only constant extra memory.

### 翻譯
**排列（permutation）** 指的是一個整數陣列的成員排列成一個序列或線性順序的方式。

例如，對於 **arr = [1,2,3]**，以下是 **arr** 的所有排列：**[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]**。
一個整數陣列的 **下一排列** 是該整數陣列的整數的下一個字典序更大的排列。更正式地說，如果將陣列的所有排列根據它們的字典序排序放入一個容器中，那麼該陣列的 **下一排列** 是在排序的容器中它的下一個排列。如果無法找到這樣的排列，則必須將陣列重新排列為最低可能的順序（即按升序排序）。

- 例如，**arr = [1,2,3]** 的下一排列是 **[1,3,2]**。
- 同樣，**arr = [2,3,1]** 的下一排列是 **[3,1,2]**。
- 而 **arr = [3,2,1]** 的下一排列是 **[1,2,3]**，因為 **[3,2,1]** 沒有字典序上更大的排列。
給定一個整數陣列 nums，找到它的下一排列。

替換必須在 **原地** 進行，並且只能使用 **恆定的額外內存**。

##### Example 1:
    Input: nums = [1,2,3]
    Output: [1,3,2]
##### Example 2:
    Input: nums = [3,2,1]
    Output: [1,2,3]
##### Example 3:
    Input: nums = [1,1,5]
    Output: [1,5,1]

##### Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100

### 想法
這題看好久還是看不懂題目意思，最後就上網查查XDDD
查完後，原來是要從所有排序中找到比現在這個數字大的排列，但也不是比他大就好，而是下一個比他大就好的，意思是像 [1,2,3] 的所有排列：[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]，但比 [1,2,3] 大一階的只有 [1,3,2]。
然而要找比較大的，只要把前面較小的和後面的的數字互換即可。但是要找大一階的，其實可以把所有排序找出來，再一一比對尋找也可以，但速度應該很可觀?
其實仔細觀察可以發現，例如 158476531，我們從十位開始，十位右邊沒有大於 3 的。 再來看百位，百位右邊沒有大於 5 的。 直到 4 ，右邊出現了很多大於 4 的，選那個剛好大於 4 的，也就是 5 。 然後交換，變成 158576431，數字變大了，但並不是剛好大於 158476531，我們還需要將 5 右邊的數字從小到大排列。 變成158513467，就可以結束了。
所以可以歸類步驟為:
1. 先從右到左找不再遞增的那一個位數
2. 找到後，和右邊的數字相比，找大一點的後，交和數字位字
3. 然後把右邊的數字排序即可
### 解法
```python
class Solution:
    def swap(self, nums: List[int], ind1: int, ind2: int) -> None:
        '''
        交換
        '''
        nums[ind1], nums[ind2] = nums[ind2], nums[ind1]
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_no_increment_num = len(nums) - 2
        # 找到第一個不再遞增的位置
        while (first_no_increment_num >= 0 and nums[first_no_increment_num + 1] <= nums[first_no_increment_num]):
            first_no_increment_num -= 1
        
        # 如果到了最左邊，就直接反向输出
        if (first_no_increment_num < 0):
            nums.reverse()
            return
        
        # 找出剛好大於的位置
        near_max_num = len(nums) - 1
        while (near_max_num >= 0 and nums[near_max_num] <= nums[first_no_increment_num]):
            near_max_num -= 1
        
        self.swap(nums, first_no_increment_num, near_max_num)

        #將後面的值排序成最小的數字
        nums[first_no_increment_num + 1::] = sorted(nums[first_no_increment_num + 1::])
```

參考:
[31. Next Permutation](https://leetcode.wang/leetCode-31-Next-Permutation.html)