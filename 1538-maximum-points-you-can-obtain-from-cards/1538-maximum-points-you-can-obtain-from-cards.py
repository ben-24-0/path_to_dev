class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        s = sum(cardPoints[:k])
        m=s
        for i in range(k):
            s = s - cardPoints[k-i-1]+cardPoints[n-i-1]
            m = max(m,s)
        return m


        