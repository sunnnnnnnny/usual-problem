# https://www.cnblogs.com/grandyang/p/6854825.html
def find(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (right - left )// 2 + left
        if nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


nums = [2, 4, 5, 6, 9]
target = 7
print(find(nums,target))