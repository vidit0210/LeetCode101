class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x = nums[:n]
        y = nums[n:]
        final = []
        for i in range(n):
            final.append(x[i])
            final.append(y[i])
        return final
