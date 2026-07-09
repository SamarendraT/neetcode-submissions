class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        b = [[] for i in range(len(nums) + 1)]

        for i in nums:
            a[i] = 1 + a.get(i, 0)
        for n, c in a.items():
            b[c].append(n)
        res = []
        for i in range(len(b)-1, 0, -1):
            for j in b[i]:
                res.append(j)
                if len(res) == k:
                    return res
            
