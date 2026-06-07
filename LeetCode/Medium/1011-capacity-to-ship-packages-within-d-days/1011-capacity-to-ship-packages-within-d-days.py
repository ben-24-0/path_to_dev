class Solution(object):
    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            day_count = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > mid:
                    day_count += 1
                    current_load = 0

                current_load += weight

            if day_count <= days:
                right = mid
            else:
                left = mid + 1

        return left