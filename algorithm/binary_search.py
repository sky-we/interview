"""
题目集合：力扣-我的收藏-二分

二分的关键点：
基本代码框架：一般使用哨兵的模式来进行检索 减少遍历次数，当left,right重合的时候就终止
1）确定搜索区间，一般使用[left, right+1) 来进行搜索
2）确定收缩区间的条件： 根据题目来决定, 有时候两边都要收缩，有时候只用收缩一边
3）确定返回值：根据题意，是返回无效值-1，还是left或right，还是left-1或right-1

"""

# 最常见的查找
# 搜索区间[left, right] 相对于哨兵模式 会额外多遍历一次
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 加一个哨兵，在相等以后就不进行遍历，遍历的区间[left, right + 1)
def binary_search_with_sentry(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1