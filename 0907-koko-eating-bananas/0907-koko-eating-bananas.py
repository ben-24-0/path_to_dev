from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hours_needed(k):
            hours = 0

            for pile in piles:
                hours += ceil(pile / k)

            return hours

        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2

            if hours_needed(mid) <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low