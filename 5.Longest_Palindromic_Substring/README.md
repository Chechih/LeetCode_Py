# 5. Longest Palindromic Substring
### 問題
Given a string s, return the longest palindromic substring in s.

 ### 翻譯
給定一個字符串 s，請返回 s 中最長的回文字串。

##### Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.
##### Example 2:
    Input: s = "cbbd"
    Output: "bb"
##### Constraints:
- 1 <= s.length <= 1000
- s consist of only digits and English letters.

### 想法
這題其實暴力法，一個 for 跑整個字串，在第二層 for 跑第二圈檢查字串是不是回文字串，就可以通過了。
然後想讓速度變快的話，可以一開始把所以字母位子記起來，之後跑兩個迴圈時，第二層只需要去檢查相同字母位子的字串即可，並且如果找到比較長的字串時，可以不要再去檢查比他短的了，這樣速度會快上許多。

### 解法
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        char_Count = len(s)
        max_rlt_leg = 0
        rlt_s = ''#回傳字串
        c_map = {}#紀錄所有字元的位子
        for i, char in enumerate(s):#記錄所有字母位子
            c_ary = c_map.setdefault(char, [])
            c_ary.append(i)
        for char, ind_ary in c_map.items():
            ind_ary.reverse()#反轉陣列，讓大的在前面
        for left, char in enumerate(s): 
            if char_Count - left <= max_rlt_leg:#如果範圍內不可能再出現更長的，不檢查了
                break
            same_char = c_map.get(char, [])#取出相同字母位子，因為左右不同字母的一定不是回文
            for right in same_char:
                leg = right - left + 1#計算長度
                if leg <= max_rlt_leg:
                    #字長度不夠，直接不檢查
                    break
                c = s[left: right + 1]#要找的範圍字串
                spilt_left = c[: leg//2]#將字串分成左右兩段
                spilt_right = c[leg//2:] if leg % 2 == 0 else c[leg//2 + 1:]
                #這邊是判斷基數時不要去抓到中間那個字元
                if spilt_left == spilt_right[::-1] and  max_rlt_leg < leg:
                    #如果左右兩邊相等就是回文了
                    max_rlt_leg = leg
                    rlt_s = c
        return rlt_s
```