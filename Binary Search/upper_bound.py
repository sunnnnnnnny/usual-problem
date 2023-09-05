# https://blog.csdn.net/u010366748/article/details/52539151
"""
在非递减数组nums中，upper_bound(nums, target)返回第一个大于target的值的位置，
如果nums中元素均小于等于target（即不存在>target的元素），
则返回nums的长度（即target如果要插入到nums中，应该插入的位置）
"""
def find1(nums,target):
    left, right = 0, len(nums) - 1
    pos = len(nums)
    while left < right:
        mid = (right - left)//2 + left
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
            pos = right

    if nums[left] > target:
        pos = left
    return pos
nums = [10, 10, 10, 20, 20, 20, 30, 30]
print(find1(nums, 9))
print(find1(nums, 10))
print(find1(nums, 15))
print(find1(nums, 20))
print(find1(nums, 25))
print(find1(nums, 30))
print(find1(nums, 40))
