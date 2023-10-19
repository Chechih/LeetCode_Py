# 28. Find the Index of the First Occurrence in a String
### 問題
Given two strings **needle** and **haystack**, return the index of the first occurrence of **needle** in **haystack**, or **-1** if **needle** is not part of **haystack**.

### 翻譯
給定兩個字串 **needle** 和 **haystack**，返回 **needle** 在 **haystack** 中第一次出現的索引，如果 **needle** 不是 **haystack** 的一部分則返回 **-1**。

##### Example 1:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6.
    The first occurrence is at index 0, so we return 0.
##### Example 2:
    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.

##### Constraints:
- 1 <= haystack.length, needle.length <= 10<sup>4</sup>
- haystack and needle consist of only lowercase English characters.

### 想法 1
直接用 find, 反正題目沒說不能用內建函式XDDD
### 解法 1
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
```

### 想法 2
建立一個 for 迴圈跑遍 haystack, 在每個字元切割出 needle 長度的字串，將切出來的字串 needle 比較，如果相等此 index 及所求，如果都沒找到回傳 -1。
### 解法 2
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_leg = len(haystack)
        needle_leg = len(needle)
        for i in range(haystack_leg):
            if i + needle_leg > haystack_leg:
                # 如果加上去的長度比 haystack 直接跳出
                break 
            if haystack[i: i + needle_leg] == needle:
                # haystack[i: i + needle_leg] 是把跟 needle 一樣長的字串切出來比較
                # 如果相等就是所求
                return i
        return -1
```