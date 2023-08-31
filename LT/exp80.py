# https://leetcode.cn/problems/uUsW3B/
"""
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution:
    def combine_sub(self,result, cache, start, n, k):
        if len(cache) == k:
            result.append(cache[:])
            return
        for i in range(start,n):
            cache.append(i)
            self.combine_sub(result, cache,i+1,n,k)
            cache.pop(-1)

    def combine(self, n: int, k: int):
        result = []
        cache = []
        self.combine_sub(result,cache, 1,n+1,k)
        return result

obj = Solution()
out = obj.combine(1,1)
print(out)