# 29. Divide Two Integers
### 問題
Given two integers **dividend** and **divisor**, divide two integers **without** using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, **8.345** would be truncated to 8, and **-2.7335** would be truncated to **-2**.

Return the **quotient** after dividing **dividend** by **divisor**.

**Note**: Assume we are dealing with an environment that could only store integers within the **32-bit** signed integer range: [-2<sup>31</sup>, 2<sup>31</sup> − 1]. For this problem, if the quotient is **strictly greater than 2<sup>31</sup> - 1**, then return **2<sup>31</sup> - 1**, and if the quotient is **strictly less than -2<sup>31</sup>**, then return **-2<sup>31</sup>**.

### 翻譯
給定兩個整數 **dividend** 和 **divisor**，在不使用乘法、除法和取模運算符的情況下，對這兩個整數進行除法運算。

整數除法應該向零截斷，這意味著失去其小數部分。例如，**8.345** 將被截斷為 **8**，**-2.7335** 將被截斷為 **-2**。

返回 **dividend** 除以 **divisor** 後的商。

**注意**：假設我們處理的環境僅能存儲 **32位** 有符號整數範圍內的整數：[-2<sup>31</sup>, 2<sup>31</sup> − 1]。對於這個問題，如果商 **嚴格大於2<sup>31</sup> - 1**，則返回 **2<sup>31</sup> - 1**，如果商嚴格小於 **-2<sup>31</sup>**，則返回 **-2<sup>31</sup>**。

##### Example 1:
    Input: dividend = 10, divisor = 3
    Output: 3
    Explanation: 10/3 = 3.33333.. which is truncated to 3.
##### Example 2:
    Input: dividend = 7, divisor = -3
    Output: -2
    Explanation: 7/-3 = -2.33333.. which is truncated to -2.

##### Constraints:
- -2<sup>31</sup> <= dividend, divisor <= 2<sup>31</sup> - 1
- divisor != 0

### 想法
這題要實作除法，題目有規定不能用內建除法，而且有規定*商*大於 2<sup>31</sup> - 1，返回 2<sup>31</sup> - 1，比  -2<sup>31</sup> 小時，返回  -2<sup>31</sup>，且他有規定 -2<sup>31</sup> <= dividend, divisor <= 2<sup>31</sup> - 1，所以如果要使用 abs 且要符合題意，必須多判斷  dividend == -2<sup>31</sup> 時，要返回 -2<sup>31</sup>。其餘的也要多判斷出來的*商*是不是負數(可以由 dividend 被除數，和 divisor 除數，其中一個是負數就是了)，這樣就可以把 dividend 和 divisor 都弄成整數來處理了，  
再來可以一直把 divisor 倍數成長到最接近 dividend 的值，且將中間 1, 2, 4, 8...倍的倍數都存起來。找到後寫個逆迴圈，將剛剛的值和她幾倍都讀出來，將他一直和 dividend 相減到 dividend 變成 0，且把剛剛倍數的值相加就是題目所求。Ex: 18/ 2 可以把 2 變成 [(1, 2), (2, 4), (4, 8), (8, 16)] 後逆迴圈跑，且建立一個值 rlt 回傳用， 先 18 - 16 剩 2, rlt 加 8， 8 和 4 都太大不理他，最後 2 - 2 等於 0 ，rlt 再加 1 = 9 就可以回傳了，如果有餘數不用管他，題目不在意。
### 解法
```python
class Solution:
    MAX_LIMIT = 2147483647
    MIN_LIMIT = -2147483648
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = False
        if dividend == self.MIN_LIMIT and divisor == -1:
            return self.MAX_LIMIT
        # 因為只有可能最小值是溢位的狀況
        if dividend < 0 or divisor < 0:
            is_negative = not (dividend < 0 and divisor < 0)
            dividend = abs(dividend)
            divisor = abs(divisor)
        # 判斷負數
        
        dic = []
        multiple = 1
        add = divisor
        while(dividend >= add):
            dic.append((multiple, add))
            multiple = multiple + multiple
            add = add + add
        # 找 divisor 的倍數
        rlt = 0
        dic = dic[::-1]
        # 翻轉後才能從大的開始減

        for (multiple, add) in dic:
            if dividend - add >= 0:
                rlt += multiple
                dividend -= add
        rlt = -rlt if is_negative else rlt 
        return rlt
```