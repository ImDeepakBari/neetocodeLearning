"""
Given an array of integers , return indices of the two numbers such that they add upto to a specific target.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15] , target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1]


"""


class Solution:

    def twoSum(self, nums, target):
        prevMap = {}  # val : index

        for i, n in enumerate(nums):

            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[n] = i

        return


answer = Solution()

sol = answer.twoSum(nums=[2, 6, 8, 22, 90], target=30)
print(sol)

sol2 = answer.twoSum(nums=[2, 6, 8, 22, 90], target=14)
print(sol2)

sol3 = answer.twoSum(nums=[2, 6, 8, 22, 90], target=92)
print(sol3)
