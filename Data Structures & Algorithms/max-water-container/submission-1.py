class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        tot = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            tot = max(area, tot)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return tot