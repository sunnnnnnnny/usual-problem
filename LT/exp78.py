# https://leetcode.cn/problems/subsets/
"""
示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
nums 中的所有元素 互不相同
"""
class Solution:
    def subsets_sub(self, result,cache,start_idx,nums):
        result.append(cache[:])
        for idx in range(start_idx,len(nums)):
            if nums[idx] not in cache:
                cache.append(nums[idx])
            self.subsets_sub(result,cache,idx+1,nums)
            cache.pop(-1)
    def subsets(self, nums):
        result = []
        cache = []
        self.subsets_sub(result,cache,0,nums)
        return result

obj = Solution()
out = obj.subsets([0])
print(out)

