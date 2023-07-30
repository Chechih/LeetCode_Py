from typing import List

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

solution = Solution()
print(solution.findMedianSortedArrays([1,2], [3,4]))