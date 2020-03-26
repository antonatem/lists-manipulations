"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

def two_nums_sum(nums, target):
    for i in range(len(nums) - 1):
        for j, v in enumerate(nums[i+1:len(nums)]):
            # import pdb; pdb.set_trace()
            if nums[i] + v == target:
                return [i, i+1+j]
            else:
                pass
