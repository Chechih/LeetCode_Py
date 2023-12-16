# 39. Combination Sum
### 問題
Given an array of **distinct** integers **candidates** and a target integer **target**, return a list of all **unique combinations** of **candidates** where the chosen numbers sum to **target**. You may return the combinations in **any order**.

The **same** number may be chosen from **candidates** an **unlimited number of times**. Two combinations are unique if the 
**frequency**
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to **target** is less than **150** combinations for the given input.

### 翻譯
給定一個包含 **獨特** 整數的陣列 **candidates** 和一個目標整數 **target**，返回所有選擇數字總和為 **target** 的 **獨特組合** 列表。你可以以 **任何順序** 返回這些組合。

相同的數字可以從 **candidates** 中 **無限次** 選擇。如果所選數字中至少一個的 **頻率** 不同，則兩個組合是獨特的。

測試案例是這樣生成的，以使總和為 **target** 的獨特組合數量少於給定輸入的 **150** 個組合。

##### Example 1:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.

##### Example 2:
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

##### Example 3:
    Input: candidates = [2], target = 1
    Output: []

##### Constraints:
- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of candidates are distinct.
- 1 <= target <= 40

### 想法
這題可以利用遞迴，寫 findCombinationSum 函式計算目前組合陣列的和，如果和 target 相等，將組合陣列加入結果清單。 在遞歸搜尋中，跑遍候選數字，嘗試不同的組合。 遞歸呼叫結束後，回溯以嘗試其他組合。
### 解法
```python
class Solution:
    def findCombinationSum(self, candidates: List[int], target: int, index: int, val_ary: List[int], rlt: List[List[int]]) -> None:
        val_sum = sum(val_ary)
        if(val_sum == target):
            rlt.append(val_ary.copy())
        for i in range(index, len(candidates)):
            if(val_sum + candidates[i] > target):
                return
            val_ary.append(candidates[i])
            self.findCombinationSum(candidates, target, i, val_ary, rlt)
            val_ary.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rlt = []
        candidates.sort()
        self.findCombinationSum(candidates, target, 0, [], rlt)
        return rlt
```