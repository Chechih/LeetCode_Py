# 4. Median of Two Sorted Arrays
### 問題
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 ### 翻譯
給定兩個已排序的數組 nums1 和 nums2，它們的大小分別為 m 和 n。請返回這兩個排序數組的中位數。

整個運算時間複雜度應為 O(log (m+n))。

##### Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.
##### Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
##### Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -106 <= nums1[i], nums2[i] <= 106

### 想法
這題其實不用想太多，因為兩個陣列都已經排序好了，所以只要準備兩個指標，一個跑 nums1，一個跑 nums2，並且隨時計算，兩個指標和是否是中位數的位子即可。  
中位數位子的算法，偶數會有兩個，然後除二，基數只有一個，那乾脆基數也當成兩個，最後除二，也是一樣的數字，減少判斷偶數基數的次數。  
EX: nums1 = [1,3], nums2 = [2] 直接取第一個位子兩次，最後除二。  
EX: nums1 = [1,2], nums2 = [3,4] 那直接抓第一個和第二個位子的值除二。


### 解法
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_leg = len(nums1)
        nums2_leg = len(nums2)
        if nums1_leg == 0 and nums2_leg == 0:#如果陣列都是空的
            return 0
        sum_leg = nums1_leg + nums2_leg#總長度
        if sum_leg == 1:#如果陣列相加是一
            return (nums1 + nums2)[0]#回傳第一個
        target_ind2 = sum_leg //2#紀錄第一個目標位子
        target_ind1 = target_ind2 if sum_leg % 2 == 1 else target_ind2 - 1#紀錄第二個目標位子
        #這裡利用總長度是基數時，中位數需要兩個數這方法下去延伸，偶數時，就把兩個數都設成相同，反正除二還是一樣的數值
        #基數時中間位子 和中間位子 -1
        target1 = None#第一個目標實際的值
        target2 = None#第二個目標實際的值
        ind = 0
        ind1 = 0#指標一，跑 nums1 用
        ind2 = 0#指標二，跑 nums2 用
        while(target1 is None or target2 is None):
            val1 = nums1[ind1] if nums1_leg > ind1 else None
            val2 = nums2[ind2] if nums2_leg > ind2 else None
            val = None
            if val2 == None or (val1 != None and val1 <= val2):
                #若 nums2 沒數值了，或是 nums1 取出的數值比較小
                ind1 += 1#往前找
                val = val1
            else:
                ind2 += 1
                val = val2
            if target_ind1 == ind:
                target1 = val
            if target_ind2 == ind:
                target2 = val          
            ind += 1
        return (target1 + target2) /2 
```