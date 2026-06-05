class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        sm=0
        totsum=0
        avgk=0
        while(i<k):
            sm  =  nums[i] +sm
            i+=1
        print(sm)
        totsum = sm/k
        
        print(sm)
        for i in range (1,len(nums)-k+1):
            sm = sm - nums[i-1]+ nums[i+k-1]
            avgk = sm/k
            totsum = max(totsum,avgk)



        return totsum