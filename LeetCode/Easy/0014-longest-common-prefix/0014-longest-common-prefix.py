class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        ref = strs[0]
        ml = len(min(strs, key=len))

        for i in range(ml):
            for s in strs:
                if s[i] != ref[i]:
                    return ref[:i]

        return ref[:ml]
