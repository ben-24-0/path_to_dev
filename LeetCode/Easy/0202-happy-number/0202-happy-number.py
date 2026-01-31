class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        
        """
        seen={}
        while(1):
            n = self.powerFn(n) 
            if n in seen:
                break
            elif (n==1):
                break
            else:
                seen[n] =True
                print(n)

        if(n==1):
            return True
        else:
            return False
    def powerFn(self,n):
        sm=0
        if n == 1:
            return 1
        while(n>0):
            rem = n%10
            sm = sm+ rem**2
            n= n//10
        return sm