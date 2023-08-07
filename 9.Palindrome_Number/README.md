# 9. Palindrome Number
### 問題
Given an integer **x**, return **true** if **x** is a ***palindrome***, and **false** otherwise.

**Follow up**: Could you solve it without converting the integer to a string?
 ### 翻譯
給定一個整數 **x**，如果 **x** 是一個 ***回文數(即正序和倒序讀都相同)*** ，則返回 **true**，否則返回 **false**。

**追問**: 您是否能夠在不將整數轉換為字符串的情況下解決這個問題？
##### Example 1:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.
##### Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
##### Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
##### Constraints:
- -2<sup>31</sup> <= x <= 2<sup>31</sup> - 1

### 想法
這一題最一開始的想法是，直接轉字串，然後去比對XDDD如下:  
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)#轉字串
        str_x_leg = len(str_x)#字串長度
        left = str_x[:str_x_leg // 2]#字串左半邊
        right = str_x[str_x_leg // 2:] if str_x_leg % 2 == 0 else str_x[str_x_leg//2 + 1:]#字串右半邊
        return right[len(right)::-1] == left#右邊反轉比對香不相等
```
然後解完也通過了，突然看到下方有一行，**追問: 您是否能夠在不將整數轉換為字符串的情況下解決這個問題？**，好吧，那我就試試不用字串解解看!?  
觀察了一下，發現其實把數字整個反轉，然後和原本的數字比對，相等他就是回文了，至於怎麼反轉呢?  
只要設定個迴圈，每次進去時，把新值乘上 10，再加上 Mode 10的舊值，且舊值每次除 10，一直反覆到把舊值歸零就反轉了。
### 解法
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False# 從範例看起來, 負號一定不是, 直接不考慮
        comparison_val = 0# 反轉後的數字
        original_val = x# 原始值存一份
        while x > 0:# 開始翻轉數字
            comparison_val *= 10
            comparison_val += x % 10
            x //= 10
        return comparison_val == original_val# 如果翻轉後的數字和原始數字相等就是回文了
```