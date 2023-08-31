#https://leetcode.cn/problems/subsets-ii/
"""
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。



示例 1：

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
"""


class Solution:
    def subsetsWithDup_sub(self, result, cache, start_idx, nums):
        result.append(cache[:])
        for idx in range(start_idx,len(nums)):
            if idx > start_idx and nums[idx] == nums[idx-1]:
                continue
            cache.append(nums[idx])
            self.subsetsWithDup_sub(result, cache,idx+1,nums)
            cache.pop(-1)
    def subsetsWithDup(self, nums):
        result = []
        cache = []
        nums.sort()
        self.subsetsWithDup_sub(result, cache, 0, nums)
        return result


obj = Solution()
out = obj.subsetsWithDup([2,2])
print(out)