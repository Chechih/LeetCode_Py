# 18. 4Sum
### 問題
Given an array **nums** of **n** integers, return an array of all the **unique** quadruplets **[nums[a], nums[b], nums[c], nums[d]]** such that:

- 0 <= a, b, c, d < n
- a, b, c, and d are **distinct**.
- nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in **any order**.
 ### 翻譯
給定一個包含 **n** 個整數的陣列 **nums**，返回所有**獨特**的四元組 **[nums[a]，nums[b]，nums[c]，nums[d]]**，滿足以下條件：

- 0 <= a, b, c, d < n
- a, b, c, 和 d **互不相同**。
- nums[a] + nums[b] + nums[c] + nums[d] == target
您可以以**任何順序**返回答案。
##### Example 1:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
##### Example 2:
    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]

##### Constraints:
- 1 <= nums.length <= 200
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>
- -10<sup>9</sup> <= target <= 10<sup>9</sup>

### 想法 
這題也是可以使用雙指標來解，步驟可以歸類為以下:  
1. 先將陣列排序，這樣就能夠使用雙指標來處理，並宣告個 rlt 變數用來記錄最接近 target 的值
2. 然後使用兩層迴圈跑遍陣列 **nums** 每個值，和指到的下一個 **nums** 值
3. 在迴圈內部使用雙指標，計算符合的值(等於 target)
4. 使用兩個指針 left 和 right，分別指向外層迴圈選擇的數字後面的元素和最後一個元素。計算 nums[i] + nums[j] + nums[left] + nums[right] 的值。
5. 如果計算的值，比目前找到的值，更接近 target ，替換掉 rlt
   如果這個值小於 target，表示需要增加總和，因此將 left 向右移動一位。
   如果這個值大於 target，表示需要減少總和，因此將 right 向左移動一位。
在使用雙指標時，要注意需要跳過重復的數字，避免重復檢查。
且可以判斷外層數字的四倍，是不是大於 target 來中止迴圈，因為已經排序過了，所以後面的數字只會越來越大
### 解法 
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        nums_leg = len(nums)
        rlt = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue  # 避免重複解
            for j in range(i + 1, nums_leg - 2):
                nn = nums[j]
                if j > i + 1 and nn == nums[j - 1]:
                    continue  # 避免重複解
                left = j + 1
                right = nums_leg - 1
                processing_target = target - n - nn
                
                while left < right:
                    total = nums[left] + nums[right]
                    if total == processing_target:
                        rlt.append([n, nn, nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1  # 避免重複解
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1  # 避免重複解
                        left += 1
                        right -= 1
                    elif total < processing_target:
                        left += 1
                    else:
                        right -= 1
            if n *4 > target:# 如果基準點的四倍比目標值大，直接放棄找，因為已經排序過，後面的數字只會越來越大
                break
                    
        return rlt
```