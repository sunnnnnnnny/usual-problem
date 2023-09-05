# https://www.cnblogs.com/grandyang/p/6854825.html
"""
这是比较常见的一类，因为我们要查找的目标值不一定会在数组中出现，也有可能是跟目标值相等的数在数组中并不唯一，
而是有多个，那么这种情况下 nums[mid] == target
这条判断语句就没有必要存在。比如在数组 [2, 4, 5, 6, 9] 中查找数字3，就会返回数字4的位置；
在数组 [0, 1, 1, 1, 1] 中查找数字1，就会返回第一个数字1的位置
"""
def find(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (right - left) // 2 + left
        if nums[mid] >= target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
    return right


nums = [2, 4, 5, 6, 9]
target = 3
print(find(nums,target))
nums = [0, 1, 1, 1, 1]
target = 1
print(find(nums,target))