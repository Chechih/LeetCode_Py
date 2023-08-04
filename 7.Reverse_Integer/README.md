# 7. Reverse Integer
### 問題
Given a signed 32-bit integer **x**, return **x** with its digits reversed. If reversing **x** causes the value to go outside the signed 32-bit integer range **[-2<sup>31</sup> , 2<sup>31</sup>  - 1]**, then return **0**.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**
 ### 翻譯
給定一個帶符號的 32 位整數 **x**，請將其數字進行反轉後返回。如果反轉 **x** 導致超出帶符號 32 位整數的範圍 **[-2<sup>31</sup> , 2<sup>31</sup>  - 1]**，則返回 **0**。

**假設環境不允許使用 64 位整數（有符號或無符號）。**

##### Example 1:
    Input: x = 123
    Output: 321
##### Example 2:
    Input: x = -123
    Output: -321
##### Example 3:
    Input: x = 120
    Output: 21
##### Constraints:
- -2<sup>31</sup> <= x <= 2<sup>31</sup> - 1

### 想法
這題其實麻煩在**假設環境不允許使用 64 位整數（有符號或無符號）**，如果沒有限制，直接字串就可以解決了，如下方程式碼:
```python
class Solution:
    max_size = 2 ** 31 - 1#32 位元最大值
    min_size = -max_size - 1 #32 位元最小值
    def reverse(self, x: int) -> int:
        abs_x = abs(x)
        str_x = str(abs_x)
        reversed_str_x = reversed(str_x)#反轉字串
        return -1 * int(reversed_str_x) if x < 0 else int(reversed_str_x)#簡查正負
```
竟然都限定了，那就必須檢查了。  
先弄一個變數 rlt，和一個迴圈，在每次進迴圈時，都把 rlt 乘 10，往上疊上去，並把值 x 都 mod 10，加上去，這樣就可以完成數字反轉。
但**假設環境不允許使用 64 位整數（有符號或無符號）**，所以再加上 x mod 10前都比需檢查，最大和最小值，怎麼檢查呢?
在弄兩個變數存最大和最小值，並且把他都除以 10，並把之前計算好的值也都除 10，這樣加上去撿就能比大小檢查有沒有炸掉了!!!

### 解法
```python
class Solution:
    max_size = 2 ** 31 - 1#32 位元最大值
    min_size = -max_size - 1 #32 位元最小值
    def reverse(self, x: int) -> int:
        rlt = 0
        abs_x = abs(x)
        is_positive = x > 0
        max_size_divide10 = self.max_size / 10#32 位元最大值除10
        min_size_divide10 = self.min_size / 10
        while(abs_x != 0):
            abs_x_mod10 = abs_x % 10 if is_positive else -(abs_x % 10)
            if max_size_divide10 < rlt + abs_x_mod10 / 10:#檢查加上去是不是比最大值大
                return 0
            if rlt + abs_x_mod10 / 10 < min_size_divide10:#檢查加上去是不是比最小值小
                return 0
            rlt = rlt *10 + abs_x_mod10#檢查通過直接加
            abs_x = abs_x //10

        return rlt
```