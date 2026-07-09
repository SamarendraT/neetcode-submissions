class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for i, n in enumerate(nums):
            k = target - n
            if k in di:
                return [di[k], i]
            di[n] = i