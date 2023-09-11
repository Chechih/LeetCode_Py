# 20. Valid Parentheses
### 問題
Given a string **s** containing just the characters **'('**, **')'**, **'{'**, **'}'**, **'['** and **']'**, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
 ### 翻譯
給定一個只包含字符 **'('**, **')'**, **'{'**, **'}'**, **'['** 和 **']'** 的字符串 **s**，判斷輸入的字符串是否有效。

輸入字符串是有效的，如果滿足以下條件：

1. 開放括號必須由相同類型的括號關閉。
2. 開放括號必須按照正確的順序關閉。
3. 每個關閉括號都有一個相應的相同類型的開放括號。
##### Example 1:
    Input: s = "()"
    Output: true
##### Example 2:
    Input: s = "()[]{}"
    Output: true
##### Example 3:
    Input: s = "(]"
    Output: false

##### Constraints:
- 1 <= s.length <= 10<sup>4</sup>
- s consists of parentheses only '()[]{}'.

### 想法 
這題可以使用堆疊，用迴圈跑字元時，將左括號全部丟進堆疊裡面，碰到右括號時，將堆疊 pop 取出，檢查左右括號是不是一組的，如果是，繼續循環直到跑完全部字元，如果不是代表此字串不是合法的括號。
### 解法 
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []# 記錄用的
        for c in s:
            if c == '(' or c == '[' or c == '{':# 左括號全部存起來
                stack.append(c)
            else:# 右括號，全部從堆疊底取出一個比對
                pop = None
                if stack:
                    pop = stack.pop()
                else:# 只有右括號
                    return False
                if c == ')' and pop != '(':
                    return False
                if c == ']' and pop != '[':
                    return False
                if c == '}' and pop != '{':
                    return False
        return len(stack) == 0 # 看看是不是空的，空的代表是完整的括號
```