# 44. Wildcard Matching
### 問題
Given an input string (**s**) and a pattern (**p**), implement wildcard pattern matching with support for **'?'** and **'*'** where:

- **'?'** Matches any single character.
- **'*'** Matches any sequence of characters (including the empty sequence).
The matching should cover the **entire** input string (not partial).

### 翻譯
給定一個輸入字串（**s**）和一個模式（**p**），實現通配符模式匹配，支持 **'?'** 和 **'*'**，其中：

- **'?'** 匹配任何單個字符。
- **'*'** 匹配任何字符序列（包括空序列）。
匹配應該覆蓋 **整個** 輸入字串（不是部分匹配）。

##### Example 1:
    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

##### Example 2:
    Input: s = "aa", p = "*"
    Output: true
    Explanation: '*' matches any sequence.

##### Example 3:
    Input: s = "cb", p = "?a"
    Output: false
    Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

##### Constraints:
- 0 <= s.length, p.length <= 2000
- s contains only lowercase English letters.
- p contains only lowercase English letters, '?' or '*'.

### 想法 1
因為題目可能會給重複的星星符號 '\*'，導致程式碼會過度深入搜尋，使效能變慢，所以一開始必須把星星符號 '\*'，一下。  
再來利用遞迴函示[call_match]，判斷給定字串 s 是否符合正則表達式 p。  
首先處理一些基本情況，如 s 或 p 為空字串時的判斷。  
接著根據正則表達式的首個字元進行不同的處理：  
- '?' 表示可以匹配任意單個字符，遞迴調用 call_match(s[1:], p[1:])。
- '*' 表示可以匹配零個或多個字符，分別遞迴調用 call_match(s[1:], p) 和 call_match(s, p[1:])。
- 如果正則表達式和字串的首個字元相等，則遞迴調用 call_match(s[1:], p[1:])。
最後還可以利用一個字典，將結果存進去，這樣可以節省重複搜尋的時間。  
### 解法 1
```python
class Solution:
    rlt_dict = {}
    def merage_star(self, p: str) ->str:
        new_p = ''
        is_start = False
        for pp in p:
            if(pp == '*' and is_start):
                continue
            if(pp == '*'):
                is_start = True
            else:
                is_start = False
            new_p += pp
        return new_p
    def call_match(self, s: str, p: str) -> bool:
        if((s, p) in self.rlt_dict):
            return self.rlt_dict[(s, p)]
        if((len(s) <= 0 and p != '*') or (len(p) <= 0 and len(s) > 0)):
            self.rlt_dict[(s, p)] = False
        elif(p[0] == '?'):
            self.rlt_dict[(s, p)] = self.call_match(s[1:], p[1:])
        elif(p[0] == '*'):
            if(p == '*'):
                self.rlt_dict[(s, p)] = True
            else:
                self.rlt_dict[(s, p)] = self.call_match(s[1:], p) or self.call_match(s, p[1:])
        elif(s[0] == p[0]):
            self.rlt_dict[(s, p)] = self.call_match(s[1:], p[1:])
        else:
            self.rlt_dict[(s, p)] = False
        return self.rlt_dict[(s, p)]

    def isMatch(self, s: str, p: str) -> bool:
        self.rlt_dict = {}
        self.rlt_dict[('','')] = True
        p = self.merage_star(p)
        rlt =  self.call_match(s, p)
        return rlt
```
### 想法 2
這題還可以使用 DP 下去解題，先建立一個二維陣列 dp 來保存中間結果，其中 dp[i][j] 表示正則表達式的前 i 個字符是否能匹配字符串的前 j 個字符。  
初始化 dp[0][0] 為 True，表示空正則表達式和空字符串是匹配的。  
動態規劃遞推：  
- 使用雙層迴圈遍歷正則表達式和字符串的每一個字符。  
- 當正則表達式 p 的第 j 個字符不是 '*' 時，則檢查前一個字符是否匹配（即 dp[j][i] = dp[j-1][i-1] and (p[j-1] == s[i-1] or p[j-1] == '?')）。  
- 當正則表達式 p 的第 j 個字符是 '' 時，則檢查 dp[j][i] = dp[j-1][i] or dp[j][i-1]，表示 '' 可以匹配零個或多個字符。  
最後返回 dp[p_leg][s_leg]，即整個正則表達式和字符串是否匹配的結果。  
### 解法 2
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_leg = len(s)
        p_leg = len(p)
        dp = [[False for i in range(len(s) + 1)] for j in range(p_leg + 1)]
        # 建 dp 用的陣列
        dp[0][0] = True
        for i in range(s_leg + 1):
            for j in range(1, p_leg + 1):# p 沒有字時，不可能匹配，直接不考慮
                if i - 1 >= 0 and p[j - 1] != '*':
                    dp[j][i] = dp[j - 1][i - 1] and (p[j - 1] == s[i - 1] or p[j - 1] == '?')
                    # 沒有 * 時，只能下去比對字串是不是相等，或是等於 ? 了
                elif p[j - 1] == '*':
                    dp[j][i] = dp[j - 1][i] or dp[j][i - 1]

        return dp[p_leg][s_leg]
```