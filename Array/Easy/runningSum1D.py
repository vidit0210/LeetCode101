class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        new_arr = []
        for i in range(len(nums)):
            sum += nums[i]
            new_arr.append(sum)
        return new_arr


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum(nums[:i+1]) for i in range(len(nums))]
