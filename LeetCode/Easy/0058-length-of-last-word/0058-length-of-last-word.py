class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        sl = s.strip().split(" ")
        l=len(sl[len(sl)-1])
        return l
        