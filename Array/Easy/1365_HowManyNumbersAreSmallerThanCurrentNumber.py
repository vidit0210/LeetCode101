class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        sorted_list = sorted(nums)
        for i, n in enumerate(sorted_list):
            if n not in d:
                d[n] = i
        return [d[n] for n in nums]
