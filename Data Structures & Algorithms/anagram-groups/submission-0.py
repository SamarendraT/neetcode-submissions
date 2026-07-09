class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        k = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')]+=1
            k[tuple(count)].append(s)
        return list(k.values())