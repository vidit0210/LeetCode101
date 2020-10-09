class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        res = start + 2*0
        for i in range(1, n):
            res ^= start + 2*i
        return res
