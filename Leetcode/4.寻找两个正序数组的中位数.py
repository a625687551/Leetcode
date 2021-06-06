#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n  = len(nums1), len(nums2)
        p1, p2 = 0, 0
        while (p1+p2) <= (m+n)/2: 
            if nums1[p1] >= nums2[p2]:
                p2 +=1
            elif nums1[p1] < nums2[p2]:
                p1 +=1
        if (m+m) %2 ==0:
            res = (nums1[p1]+nums2[p2])/2
        else:
            res = 
        return 



# @lc code=end

