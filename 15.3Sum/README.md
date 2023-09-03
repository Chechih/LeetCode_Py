# 15. 3Sum
### 問題
Given an integer array nums, return all the triplets **[nums[i], nums[j], nums[k]]** such that **i != j**, **i != k**, and **j != k**, and **nums[i] + nums[j] + nums[k] == 0**.

Notice that the solution set must not contain duplicate triplets.
 ### 翻譯
給定一個整數陣列 nums，返回所有滿足條件 **i != j**、**i != k**、**j != k** 以及 **nums[i] + nums[j] + nums[k] == 0** 的三元組 **[nums[i]，nums[j]，nums[k]]**。

請注意，解答集合不能包含重複的三元組。
##### Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.
##### Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.
##### Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.
##### Constraints:
- 3 <= nums.length <= 3000
- -10<sup>5</sup> <= nums[i] <= 10<sup>5</sup>

### 想法  
這題可以使用雙指標來解，步驟可以歸類為以下:  
1. 先將陣列排序，這樣就能夠使用雙指標來處理
2. 然後使用一個迴圈跑遍陣列 **nums** 每個值
3. 在迴圈內部使用雙指標，計算符合的值(等於 0)
4. 使用兩個指針 left 和 right，分別指向外層迴圈選擇的數字後面的元素和最後一個元素。計算 nums[i] + nums[left] + nums[right] 的值。
5. 如果計算的值，等於零，將值存在返回的陣列中  
   如果這個值小於 0，表示需要增加總和，因此將 left 向右移動一位。
   如果這個值大於 0，表示需要減少總和，因此將 right 向左移動一位。
在使用雙指標時，要注意需要跳過重復的數字，避免重復檢查。
且可以判斷外層數字的三倍，是不是大於零來中止迴圈，因為已經排序過了，所以後面的數字只會越來越大
### 解法 
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_leg = len(nums)
        rlt = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue  # 避免重複解
            
            left = i + 1
            right = nums_leg - 1
            target = -n
            
            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    rlt.append([n, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # 避免重複解
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # 避免重複解
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
            if n *3 > 0:# 如果基準點的三倍比目標值大，直接放棄找，因為已經排序過，後面的數字只會越來越大
                break
                    
        return rlt
```