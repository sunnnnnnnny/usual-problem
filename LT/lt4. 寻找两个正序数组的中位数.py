# https://leetcode.cn/problems/median-of-two-sorted-arrays/
"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。



示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

"""

class Solution:
    def find_k_max(self, nums1, nums2, i, j, len1, len2, k):
        if i >= len1:
            return nums2[j + k - 1]
        if j >= len2:
            return nums1[i + k - 1]
        if k == 1:
            return min(nums1[i], nums2[j])
        val1 = nums1[i + k//2 - 1] if i + k // 2 - 1< len1 else float("inf")
        val2 = nums2[j + k//2 - 1] if j + k // 2 - 1< len2 else float("inf")
        if val1 < val2:
            return self.find_k_max(nums1, nums2, i + k // 2, j, len1, len2, k - k // 2) # 应该是从i+k//2索引开始，因为i+k//2-1索引已经使用
        else:
            return self.find_k_max(nums1, nums2, i, j + k // 2,len1, len2, k - k //2 )
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        mid1 = (len(nums1) + len(nums2) + 1) // 2
        mid2 = (len(nums1) + len(nums2) + 2) // 2
        res1 = self.find_k_max(nums1, nums2, 0, 0,len(nums1),len(nums2),mid1)
        res2 = self.find_k_max(nums1, nums2, 0, 0,len(nums1),len(nums2),mid2)
        return (res1+res2) / 2
    def findMedianSortedArrays_merge(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        mid1 = (len(nums) + 1) // 2
        mid2 = (len(nums) + 2) // 2
        return (nums[mid1 - 1] + nums[mid2 - 1]) / 2


obj = Solution()
nums1 = [1,3]
nums2 = [2]
print(obj.findMedianSortedArrays(nums1,nums2))
nums1 = [1,2]
nums2 = [3,4]
print(obj.findMedianSortedArrays(nums1,nums2))
