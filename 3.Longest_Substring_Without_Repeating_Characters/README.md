# 3. Longest Substring Without Repeating Characters
### 問題
Given a string s, find the length of the longest substring without repeating characters.

 ### 翻譯
給定一個字符串s，找到最長的不含重複字符的子串的長度。

##### Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
##### Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
##### Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
##### Constraints:
- 0 <= s.length <= 5 * 104
- s consists of English letters, digits, symbols and spaces.

### 想法 1
這題最直覺的方法應該是用兩個迴圈，一個負責跑 s，一個負責檢查往後比對長度和有沒有重複，有的話直接比對下一個字串。

### 解法 1
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        charCount = len(s)
        spilt = ''#紀錄這個字串到下個重複的字串的變數
        max_rlt = 1 if charCount > 0 else 0#初始回傳 max_rlt
        for i, char in enumerate(s): 
            spilt = char
            for j in range(i + 1, charCount):
                char = s[j]
                if(char in spilt):#如果在切的字串內(重複了)
                    break
                else:
                    spilt += char
                max_rlt = max(max_rlt, len(spilt))#抓最大的
        return max_rlt
```

### 想法 2
雖然*想法一*可以解出來，不過速度真的慢XDDD  
後面上網找了下，可以使用 Sliding Window(滑動視窗)的方法下去解。  
>Sliding Window(滑動視窗): 透過使用一個可變的視窗大小或固定視窗大小來解題，通常多用在字串或陣列的問題

![Sliding Window](https://chechih.github.io/images/LeetCode/Sliding_Window_Sample.gif "Sliding Window")  
那要怎麼套用呢?  
一開始要先用一個 List 紀錄出現過的字元(等等會用 set，檢查字元比較快)，和一個變數紀錄左邊位子(變數名:left)，位自從零開始，然後用 for 迴圈掃字串，然後把出現過的字元丟進 List 裡，如果掃到重複的字元，left 變數加一，一直掃到一直加一(指標往右)，這樣就可以知道此刻這個字元被包含的最大字串，可能有點抽象@@  
上圖:  
![3. Longest Substring Without Repeating Characters](https://chechih.github.io/images/LeetCode/3_Sample.jpg "3. Longest Substring Without Repeating Characters")  
左邊的其實就是現在最多能找到的不重複的字元

### 解法 2
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        numset = set()#存出現過的字元
        left = 0#現在出現過的最常字元初始位子
        max_rlt = 0
        for i, char in enumerate(s):
            while char in numset:#如果現在的字元在之前找到的字串上，一直往右移，直到都沒有
                numset.remove(s[left])
                left += 1
            numset.add(char)
            max_rlt = max(max_rlt, i - left + 1)
        return max_rlt
```

參考:  
[滑動視窗(Sliding Window)](https://hackmd.io/@SupportCoding/Sliding_Window)  
[JS | 98% | Sliding window | With exlanation](https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/2694302/js-98-sliding-window-with-exlanation/)