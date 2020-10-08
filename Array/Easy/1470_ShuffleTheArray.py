# class Solution(object):
#     def shuffle(self, nums, n):
#         """
#         :type nums: List[int]
#         :type n: int
#         :rtype: List[int]
#         """
#         x = nums[:n]
#         y = nums[n:]
#         final = []
#         for i in range(n):
#             final.append(x[i])
#             final.append(y[i])
#         return final


class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        output = []
        i = 0
        j = n
        while i < n:
            output.append(nums[i])
            output.append(nums[j])
            i += 1
            j += 1
        return output
