class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums=[]
        n=len(matrix[0])
        for i in range(len(matrix)):
            nums+=matrix[i][:n]
        low=0
        high=len(nums)-1
        while low<=high:
            avg=(low+high)//2
            if target==nums[avg]:
                return True
            elif nums[avg]<target:
                low=avg+1
            elif nums[avg]>target:
                high=avg-1
        return False