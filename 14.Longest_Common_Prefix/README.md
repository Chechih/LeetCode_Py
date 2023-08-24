# 14. Longest Common Prefix
### 問題
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string **""**.
 ### 翻譯
撰寫一個函式來在一個字符串陣列中找到最長的共同前綴字串。

如果沒有共同前綴，則返回一個空字串 **""**。
##### Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
##### Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
##### Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- **strs[i]** consists of only lowercase English letters.

### 想法 
這題可以直接以地一個字串當基準，從零開始比對其他字串，直到出現不不相同的即可。
### 解法 
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_leg = len(strs)
        rlt = ''
        if strs_leg < 1:# 沒有字串直接回傳空字串
            return rlt
        first_str = strs[0]
        strs.remove(first_str)
        for i, fc in enumerate(first_str): 
            is_same = True
            for s in strs:
                if len(s) <= i or s[i] != fc:# 檢查每個字串是不是都相同
                    is_same = False
                    break
            if not is_same:
                break
            rlt += fc
        return rlt
```