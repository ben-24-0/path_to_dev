class Solution:
    def nodays(self,weights,cap):
        day,load=1,0
        for i in range(0,len(weights)):
            if(load+weights[i]>cap):
                day+=1
                load=weights[i]
            else:
                load+=weights[i]
        return day
    def shipWithinDays(self, weights, days):
        # Your code goes here
        
        low=max(weights)
        high = sum(weights)
        while(low<=high):
            mid=(low+high)//2
            nod = self.nodays(weights,mid)
            if(nod<=days):
                high=mid-1
            else:
                low = mid+1
        return low
