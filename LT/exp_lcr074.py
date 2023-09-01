# https://leetcode.cn/problems/SsGoHC/
"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。



示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""

class Solution:
    def cmp(self, nums1, nums2):
        if nums1[0] < nums2[0]:
            return 1
        elif nums1[0] > nums2[0]:
            return 0
        else:
            if nums1[1] < nums2[1]:
                return 1
            else:
                return 0
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x:[x[0],x[1]])
        result = []
        for interval in intervals:
            if len(result) == 0:
                result.append(interval)
            start, end = interval
            if start == end:
                if start < result[-1][1]:
                    continue
                else:
                    result[-1][1] = start
            if start < result[-1][1]:
                if start >= result[-1][0]:
                    if end <= result[-1][1]:
                        continue
                    else:
                        result[-1][1] = end

                else:
                    if end >=
            elif start == result[-1][1]
                pass
            else:
                pass
        print(intervals)

obj = Solution()
obj.merge(intervals = [[2,6],[1,3],[8,10],[1,4], [15,18]])