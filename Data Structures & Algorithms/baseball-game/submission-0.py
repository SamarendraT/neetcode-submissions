class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a = []
        b = 0
        for i in operations:
            if i == "+":
                b += a[-1] + a[-2]
                a.append(a[-1] + a[-2]) 
            elif i == "D":
                a.append(a[-1] * 2)
            elif i == "C":
                a.pop()
            else:
                a.append(int(i))
            
        return sum(a)