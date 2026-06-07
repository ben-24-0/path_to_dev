class Solution:
    # def nodays(self,weights,cap):
    #     day,load=1,0
    #     for i in range(0,len(weights)):
    #         if(load+weights[i]>cap):
    #             day+=1
    #             load=weights[i]
    #         else:
    #             load+=weights[i]
    #     return day
    def shipWithinDays(self, weights, days):
        # Your code goes here
        def nodays(capacity):
            days_used = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > capacity:
                    days_used += 1
                    current_load = weight
                else:
                    current_load += weight

            return days_used       
        low=max(weights)
        high = sum(weights)
        while(low<=high):
            mid=(low+high)//2
            nod = nodays(mid)
            if(nod<=days):
                high=mid-1
            else:
                low = mid+1
        return low
