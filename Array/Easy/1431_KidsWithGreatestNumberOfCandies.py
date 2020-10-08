class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        if not candies:
            return []
        m = candies[0]
        for c in candies:
            if c > m:
                m = c
        return [c + extraCandies >= m for c in candies]
