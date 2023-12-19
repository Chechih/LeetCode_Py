# 41. First Missing Positive
### 問題
Given an unsorted integer array **nums**, return the smallest missing positive integer.

You must implement an algorithm that runs in **O(n)** time and uses **O(1)** auxiliary space.

### 翻譯
給定一個未排序的整數陣列 **nums**，返回最小的缺失正整數。

你必須實現一個在 **O(n)** 時間內運行且使用 **O(1)** 輔助空間的演算法。

##### Example 1:
    Input: nums = [1,2,0]
    Output: 3
    Explanation: The numbers in the range [1,2] are all in the array.

##### Example 2:
    Input: nums = [3,4,-1,1]
    Output: 2
    Explanation: 1 is in the array but 2 is missing.

##### Example 3:
    Input: nums = [7,8,9,11,12]
    Output: 1
    Explanation: The smallest positive integer 1 is missing.

##### Constraints:
- 1 <= nums.length <= 10<sup>5</sup>
- -2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1

### 想法 1
這題如果不管題目的時間和空間複雜度的話，可以把 nums 也轉成 set，然後建一個 set，內容 1 到 nums_leg + 2 ，再和剛剛的 nums set 相減，然後找出最小的正整數就好。
### 解法 1
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_leg = len(nums)
        rule = set(range(1, nums_leg + 2))
        diff = rule - set(nums)
        if(len(diff) > 0):
            return min(diff)
        else:
            return 1
```
### 想法 2
不過這題想了很久還是參考了網路上的解法XDDD  
步驟可以歸類為
1. 指定變數 nums_leg = len(nums)
2. 將 nums 小於 0 和大於 nums_leg 的設定標記，也就是用一個數字取代掉，這邊用 nums_leg + 1
3. 透過將該數字的索引轉換為負數來標記數組中出現的每個單元格，利用 nums 陣列來標記出現過的，出現過的都轉成負數，這樣就能從位子找出最小正整數了
4. 找出第一個非負數的儲存格（沒有出現在陣列中），找陣列值大於 0 的位子，因為剛剛都有標記出現過的都設定成負數了
5. 沒有找到正數，這表示數組包含所有數字 1..n，所以回傳 nums_leg + 1
### 解法 2
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 1. 指定 nums_leg

        nums_leg = len(nums)

        # 2. 以特殊標記編號 (n+1) 標記編號 (num < 0) 和 (num > n)
        # （我們可以忽略這些，因為如果所有數字都 > n 那麼我們將簡單地傳回 1）
        for i in range(nums_leg):
            if nums[i] <= 0 or nums[i] > nums_leg:
                nums[i] = nums_leg + 1

        # 數組中的所有數字現在都是正數，且範圍為 1..n+1
    
        # 3. 透過將該數字的索引轉換為負數來標記數組中出現的每個單元格
        for i in range(nums_leg):
            num = abs(nums[i])
            if num > nums_leg:
                continue
            num -= 1
            # -1 表示基於零索引的陣列（因此數字 1 將位於位子 0）
            if nums[num] > 0:
                # 防止雙重否定運算
                nums[num] = -1 * nums[num]
            
        # 4. 找出第一個非負數的儲存格（沒有出現在陣列中）
        for i in range(nums_leg):
            if nums[i] >= 0:
                return i + 1
    
        # 5. 沒有找到正數，這表示數組包含所有數字 1..n
        return nums_leg + 1
```

參考:  
[Java - simple solution - with documentation](https://leetcode.com/problems/first-missing-positive/solutions/17214/java-simple-solution-with-documentation/)  