class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def isEven(n):
            return 1 if len(str(n)) % 2 == 0 else 0
        c = 0
        for num in nums:
            c += isEven(num)
        return c
