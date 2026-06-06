class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums=[]
        for i in range(len(matrix)):
            nums+=matrix[i][:len(matrix[i])]
        low=0
        high=len(nums)-1
        inx=0
        while low<=high:
            avg=(low+high)//2
            if target==nums[avg]:
                inx=avg
                return True
            elif nums[avg]<target:
                low=avg+1
            elif nums[avg]>target:
                high=avg-1
        return False