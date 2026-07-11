class Solution:
    def isValid(self, s: str) -> bool:
        di = {"}":"{", "]" : "[", ")" : "("}
        st = []
        for i in s:
            if i in di:
                if st and st[-1] == di[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
            
        return True if not st else False