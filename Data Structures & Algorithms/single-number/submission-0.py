class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from functools import reduce
        ans = reduce(lambda x, y: x^y, nums, 0)
        return ans