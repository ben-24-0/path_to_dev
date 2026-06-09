class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk=[]
        res=[0]*n
        for i in range(len(temperatures)-1,-1,-1):
            while(stk and temperatures[stk[-1]]<=temperatures[i]):
                stk.pop()
            if stk:
                res[i] = stk[-1]-i
            stk.append(i)
        return  res



            

