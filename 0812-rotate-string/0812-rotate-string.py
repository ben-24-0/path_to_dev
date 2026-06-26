from collections import Counter
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return Counter(s) == Counter(goal)
