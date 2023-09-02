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
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x:[x[0],x[1]])
        result = []
        for interval in intervals:
            if len(result) == 0:
                result.append(interval)
                continue
            start, end = interval
            if start == end:
                if start <= result[-1][1]:
                    continue
                else:
                    result.append(interval)
            else:
                if start <= result[-1][1]:
                    if end > result[-1][1]:
                        result[-1][1] = end
                else:
                    result.append(interval)
        return result

obj = Solution()
print(obj.merge(intervals = [[2,6],[1,3],[8,10],[1,4], [15,18]]))
print(obj.merge(intervals = [[1,4],[4,5]]))
print(obj.merge(intervals = [[1,4],[2,3]]))
print(obj.merge(intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))