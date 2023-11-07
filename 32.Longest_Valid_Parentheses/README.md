# 32. Longest Valid Parentheses
### 問題
Given a string containing just the characters **'('** and **')'**, return the length of the longest valid (well-formed) parentheses **substring**.

### 翻譯
給定一個只包含字符 **'('** 和 **')'** 的字串，返回最長有效（合法形式）括號 **子字串** 的長度。

##### Example 1:
    Input: s = "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()".
##### Example 2:
    Input: s = ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()".
##### Example 3:
    Input: s = ""
    Output: 0

##### Constraints:
- 0 <= s.length <= 3 * 10<sup>4</sup>
- s[i] is '(', or ')'.

### 想法1
這題一開始想到的解法是用兩個變數(left,  right)，來記錄左右括號的數目，然後當左右括號(left,  right)，都相等時，更新要回傳的變數，且右括號數目大於左括號數目時，將變數(left,  right)都設定成 0，因為代表這不可能形成有效的括號，但是對於'(()'這總 CASE 時，沒辦法更新值，那怎麼辦呢? 答案是反向用相同的做法再掃ㄧ次即可，像剛剛的 CASE '(()' ==> '())'，就可以掃到括號了。
### 解法1
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left_parentheses = 0
        # 紀錄左誇號
        right_parentheses = 0
        max_leg = 0
        # 找最大合法值
        for c in s:
            if c == '(':
                left_parentheses += 1
            else:
                right_parentheses += 1
            if left_parentheses == right_parentheses:
                max_leg = max(max_leg, right_parentheses * 2)
            if left_parentheses < right_parentheses:
                left_parentheses = right_parentheses = 0
        left_parentheses = right_parentheses = 0
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == '(':
                left_parentheses += 1
            else:
                right_parentheses += 1
            if left_parentheses == right_parentheses:
                max_leg = max(max_leg, left_parentheses * 2)
            if left_parentheses > right_parentheses:
                left_parentheses = right_parentheses = 0
        
        return max_leg
```
### 想法2
再來這想法是參考網路上別人的作法的，先用一個堆疊(stack)，將所有的遇到的左括號位子存進去，如果遇到右括號時，先將對應的括號移出，然後有兩種狀況:
1. 堆疊(stack)是空時: 將現在的位子加進去，代表他是新的起始點
2. 堆疊(stack)不是空時: 就用目前的位置減去堆疊(stack)頂的存的位置，然後就得到當前合法序列的長度，然後更新一下最長長度。代表左誇號是連在一起的所以直接減去他的前一位
### 解法2
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        rlt = 0
        stack = []
        stack.append(-1)
        # 先加入 -1 為了讓後面好計算
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                # 取出對應的左誇號
                if (not stack):
                    stack.append(i)
                    # 新的起始點
                else:
                    rlt = max(rlt, i - stack[-1])
                    # 因為 stack 不是空的代表左誇號是連在一起的所以直接減去他的前一位

        return rlt
```

參考:  
[32. Longest Valid Parentheses](https://leetcode.wang/leetCode-32-Longest-Valid-Parentheses.html)  