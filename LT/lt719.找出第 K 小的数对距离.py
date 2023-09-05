# https://leetcode.cn/problems/find-k-th-smallest-pair-distance/
"""
数对 (a,b) 由整数 a 和 b 组成，其数对距离定义为 a 和 b 的绝对差值。

给你一个整数数组 nums 和一个整数 k ，数对由 nums[i] 和 nums[j] 组成且满足 0 <= i < j < nums.length 。返回 所有数对距离中 第 k 小的数对距离。



示例 1：

输入：nums = [1,3,1], k = 1
输出：0
解释：数对和对应的距离如下：
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
距离第 1 小的数对是 (1,1) ，距离为 0 。
示例 2：

输入：nums = [1,1,1], k = 2
输出：0
示例 3：

输入：nums = [1,6,1], k = 3
输出：5

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2
"""

class Solution:
    def smallestDistancePair_brute_force(self, nums, k: int):
        diff_abs = []
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                diff_abs.append(abs(nums[j]- nums[i]))
        diff_abs.sort()
        return diff_abs[k-1]

    def smallestDistancePair_bucket_sort(self,nums, k: int):
        buckets = [0 for _ in range(1000*1000+1)]
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                diff_abs = abs(nums[j] - nums[i])
                buckets[diff_abs] = buckets[diff_abs] + 1
        for i in range(len(buckets)):
            bucket = buckets[i]
            if k - bucket <= 0:
                return i
            k = k - bucket
        return -1
    def smallestDistancePair(self, nums, k: int):
        nums.sort()


obj = Solution()
print(obj.smallestDistancePair_bucket_sort(nums = [1,3,1], k = 3))
