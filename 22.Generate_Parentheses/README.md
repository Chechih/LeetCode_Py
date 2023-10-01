# 22. Generate Parentheses
### 問題
Given **n** pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 ### 翻譯
給定 **n** 對括號，編寫一個函數來生成所有合法括號的組合。
##### Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
##### Example 2:
    Input: n = 1
    Output: ["()"]

##### Constraints:
- 1 <= n <= 8

### 想法 
這題可以使用遞迴，傳入左括號，右括號數量，和一個紀錄的 array，然後根據以下步驟:
1. 檢查左括號，是否大於零。如果是的話，將現在狀態(括號的排列)加上一個左括號，且左括號數量減一，往下繼續遞迴
2. 檢查右括號，是否大於零，且右括號數量要大於左括號數量。如果是的話，將現在狀態(括號的排列)加上一個右括號，且右括號數量減一，往下繼續遞迴
3. 如果左右括號數量都使用完畢(等於 0)時，將現在狀態(括號的排列)，存進陣列裡
### 解法 
```python
class Solution:
    def getCombination(self, lParentheses: int, rParentheses: int, combination: List[str], nowParenthes: str = '') -> None:
        if(lParentheses > 0):
            self.getCombination(lParentheses -1, rParentheses, combination, nowParenthes + '(')
        if(rParentheses > 0 and lParentheses < rParentheses):
            self.getCombination(lParentheses, rParentheses - 1, combination, nowParenthes + ')')
        if(lParentheses == 0 and rParentheses == 0):
            combination.append(nowParenthes)
        
    def generateParenthesis(self, n: int) -> List[str]:
        combination = []
        self.getCombination(n, n, combination)
        return combination
```