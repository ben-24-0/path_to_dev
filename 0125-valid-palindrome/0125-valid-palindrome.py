import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=re.findall("[a-zA-Z0-9]",s)
        pl="".join(st).lower()
        st.reverse()
        pr = "".join(st).lower()
        print(pl,pr)
        if(pl==pr ):
            return True
        else:
            return False


