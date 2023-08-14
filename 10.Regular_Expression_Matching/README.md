# 10. Regular Expression Matching
### 問題
Given an input string **s** and a pattern **p**, implement regular expression matching with support for **'.'** and **'*'** where:

**'.'** Matches any single character.​​​​
**'*'** Matches zero or more of the preceding element.
The matching should cover the **entire** input string (not partial).
 ### 翻譯
給定輸入字符串 **s** 和模式字符串 **p**，請實現支持 **'.'** 和 **'*'** 的正則表達式匹配，其中：

**'.'** 可以匹配任意單個字符。
**'*'** 可以匹配零個或多個前面的元素。
匹配應該覆蓋**整個**輸入字符串（不能是部分匹配）。
##### Example 1:
    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
##### Example 2:
    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
##### Example 3:
    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".
##### Constraints:
- 1 <= s.length <= 20
- 1 <= p.length <= 20
- **s** contains only lowercase English letters.
- **p** contains only lowercase English letters, **'.'**, and **'*'**.
- It is guaranteed for each appearance of the character **'*'**, there will be a previous valid character to match.

### 想法 1
這問題一開始想到的，是直接用使用 **'遞迴'** 的方式下去解，因為題目有 **'.'** 代表任何數字，而 **'*'** 則是上一個數字， **重複 N 次(N 可能是 0)** 。  
比如 s = 'a', 和 p = 'ab*' 是相等的，因為 * 可以讓 b 不出現，所以變成 s = 'a'，和 p = 'a'，且 s = 'abb', 和 p = 'ab*' ，也是相等的，因為 * 可以讓他出現兩次，變成 s = 'abb'，和 p = 'abb'。  
而 '.' 更特殊了，他可以變成任何字元，有點類似撲克牌中的 Joker(鬼牌)，所以你有一串 s = 'abcdefg'， p = '.*'，他們是相等的!?  
那 **'遞迴'** 整理出來的邏輯如下
- 先檢查到最後 s 和 p 是不是空字串(字串被消耗完畢的狀況)，那他一定是相等的!?回傳 True
- 再來比對 s 的第二個字字源是不是 '*'，如果是可能出現兩種狀況
  - s 的第一個字元和 p 的第一個字元相等時，或是 p 的第一個字元是'.'(任意字元)，他可能消耗到 s 第一個字元，或是把 p 前面兩個字元(N 和 *)[N 是第一個字元]消耗掉，繼續'遞迴'
  - 如果不相等，那只能把 p 前面兩個拿掉(* = 0)，繼續'遞迴'
- 再來是判斷不是 '*'時，就只能比對 s 的第一個字元，和 p 的第一個字元是不是相等，或是 p 是不是 '.'，來把字元消耗掉
- 最後都不是上面的狀況，代表他們不匹配，直接回傳 False
### 解法 1
```python
class Solution:
class Solution:
    def run_isMatch(self, s: str, p: str) -> bool:
        s_leg = len(s)
        p_leg = len(p)
        if s == '' and p == '':
            return True
        if p_leg > 1 and p[1] == '*':
            if s_leg > 0 and (s[0] == p [0] or p [0] =='.'):
                return self.run_isMatch(s[1::], p) or self.run_isMatch(s, p[2::])
                #如果 p 第二個字是 *, 則可能是 s 第一個字, 或是完全沒匹配直接拿掉兩種可能
            else:
                #如果地一個字完全不同, 那一定要拿掉 p
                return self.run_isMatch(s, p[2::])
        if s_leg > 0 and p_leg > 0 and (s[0] == p [0] or p [0] =='.'):
            return self.run_isMatch(s[1::], p[1::])
        return False
    
    def isMatch(self, s: str, p: str) -> bool:
        p_ary = []# 用來把重複的正規清掉比如 a*a*a*a* -> a*
        for pc in p:
            if pc != '*':
                p_ary.append(pc)
            else:
                last = p_ary.pop()
                if len(p_ary) == 0 or (p_ary[-1] != last + '*'):
                    p_ary.append(last + '*')
        return self.run_isMatch(s, ''.join(p_ary))
```

### 想法 2
再來這題也可以使用 DP (動態規劃)，下去解，只是要找到規律，要先定義一個二維陣列，X 列是 s 字串的長度，Y 列是 p 字串的長度，所以 dp[i][j] 是 s[0:j:] 和 p[0:i:]，又有下三種狀況:  
-  if p[i - 1] != '*' 時，dp[i][j] = dp[i - 1][j - 1] and (p[i - 1] == s[j - 1] || p[i - 1] == '.');
-  if p[i - 1] == '*' 時，第一種狀況是 dp[i][j] = dp[i - 2][j]， * 重複 0 次時
-  if p[i - 1] == '*' 時，第二種狀況是 dp[i][j] = dp[i][j - 1] and (s[j - 1] == p[i - 2] or p[i - 2] == '.')， * 重複 1 次以上時
複上圖片比較能理解!?  
圖片範例是 p = "mississippi", s = "mis*is*ip*."
![10. Regular Expression Matching Sample](https://chechih.github.io/images/LeetCode/10.Regular_Expression_Matching_Sample.png "10. Regular Expression Matching Sample")  
圖片來源: [🚀 ✅ Detailed explaination 🔥 with Pictures ✅ 🔥 🚀 in C++,Java , Python , DP bottom up tabulation.](https://leetcode.com/problems/regular-expression-matching/solutions/3401751/detailed-explaination-with-pictures-in-c-java-python-dp-bottom-up-tabulation/)  

### 解法 2
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_leg = len(s)
        p_leg = len(p)
        dp = [[False for i in range(s_leg + 1)] for j in range(p_leg + 1)]
        # 建 dp 用的陣列
        dp[0][0] = True
        for j in range(s_leg + 1):
            for i in range(1, p_leg + 1):# p 沒有字時，不可能匹配，直接不考慮
                if i - 1 >= 0 and p[i - 1] != '*':
                    dp[i][j] = dp[i - 1][j - 1] and (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                    # 沒有 * 時，只能下去比對字串是不是相等，或是等於 . 了
                elif i - 2 >= 0:
                    dp[i][j] = dp[i - 2][j]
                    # * 重複 0 次時
                    dp[i][j] = dp[i][j] or (dp[i][j - 1] and (s[j - 1] == p[i - 2] or p[i - 2] == '.'))
                    # * 重複 1 次以上時

        return dp[p_leg][s_leg]
```
### 想法 3
直接作弊用正規表達式的套件XDDDD
### 解法 3
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        finded = re.findall(p, s)
        return len(finded) > 0 and finded[0] == s
```

參考:  
[🚀 ✅ Detailed explaination 🔥 with Pictures ✅ 🔥 🚀 in C++,Java , Python , DP bottom up tabulation.](https://leetcode.com/problems/regular-expression-matching/solutions/3401751/detailed-explaination-with-pictures-in-c-java-python-dp-bottom-up-tabulation/)  
[C++ O(n)-space DP](https://leetcode.com/problems/regular-expression-matching/solutions/5684/c-on-space-dp/)  
[[LeetCode] 10. Regular Expression Matching 正则表达式匹配](https://www.cnblogs.com/grandyang/p/4461713.html)  