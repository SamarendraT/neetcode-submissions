class Solution:

    def encode(self, strs: List[str]) -> str:
        s = []
        for i in strs:
            a = str(len(i)) + '#' + i
            s.append(a)
        return ''.join(s)

    def decode(self, s: str) -> List[str]:

        k = []
        i = 0
        while i <  len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            k.append(s[i:j])
            i = j

        return k