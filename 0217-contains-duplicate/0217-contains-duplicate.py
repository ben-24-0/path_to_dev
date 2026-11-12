class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0)+1
        for val in freq.values():
            if val >1:
                return True
        return False