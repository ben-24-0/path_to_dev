class Solution(object):
    def toRome(self, s, i):
        if s[i] == "I": return 1
        elif s[i] == "V": return 5
        elif s[i] == "X": return 10
        elif s[i] == "L": return 50
        elif s[i] == "C": return 100
        elif s[i] == "D": return 500
        elif s[i] == "M": return 1000

    def romanToInt(self, s):
        i = 0
        sm = 0

        while i < len(s) - 1:
            if self.toRome(s, i) >= self.toRome(s, i + 1):
                sm += self.toRome(s, i)
                i += 1
            else:
                sm += self.toRome(s, i + 1) - self.toRome(s, i)
                i += 2

        # 🔥 end-case fix
        if i < len(s):
            sm += self.toRome(s, i)

        return sm
