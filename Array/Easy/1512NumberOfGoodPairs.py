# class Solution(object):
#     def numIdenticalPairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         num_pairs = 0
#         for i in range(len(nums)):
#             for j in range(1, len(nums)):
#                 if nums[i] == nums[j] and i < j:
#                     num_pairs += 1
#         return num_pairs


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        c = 0
        for n in nums:
            c += d.get(n, 0)
            d[n] = d.get(n, 0)+1
        return c
