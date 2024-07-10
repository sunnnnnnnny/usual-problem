# ref: https://blog.csdn.net/airenKKK/article/details/105311680
class Solution:
    def __init__(self):
        pass

    def trap(self, heights):
        if len(heights) == 0:
            return 0
        max_element_idx = heights.index(max(heights))
        cur_left, cur_right, res = 0, 0, 0
        for i in range(0, max_element_idx, 1):
            if heights[i] > cur_left:
                cur_left = heights[i]
            else:
                res = res + cur_left - heights[i]
        for j in range(len(heights)-1, max_element_idx, -1):
            if heights[j] > cur_right:
                cur_right = heights[j]
            else:
                res = res + cur_right - heights[j]
        return res


sol_obj = Solution()
input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
out = sol_obj.trap(input)
print(out)
