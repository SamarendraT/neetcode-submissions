class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        c = 0
        for i in nums:
            if (i-1) not in numset:
                length = 1
                while (i+length) in numset:
                    length+=1
                c = max(c, length)
        return c