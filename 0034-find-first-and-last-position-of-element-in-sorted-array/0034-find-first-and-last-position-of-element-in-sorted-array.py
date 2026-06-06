class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        x = -1
        y = -1
        while low <= high:
            avg = (low + high) // 2
            if nums[avg] == target:
                x = avg
                y = avg
                while x - 1 >= 0 and nums[x - 1] == target:
                    x -= 1
                while y + 1 < len(nums) and nums[y + 1] == target:
                    y += 1
                break
            elif nums[avg] < target:
                low = avg + 1
            else:
                high = avg - 1
        return [x, y]