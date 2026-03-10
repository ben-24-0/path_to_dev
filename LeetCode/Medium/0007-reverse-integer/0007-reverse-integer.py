class Solution(object):
    def reverse(self, x):
        rev = 0
        flag=0
        if(x<0):
            x*=-1
            flag =1
        
        org = x
        rev =0
        while(x>0):
            rem = x%10
            rev = rev * 10 + rem
            x = x//10
        if (flag):
            rev = rev * -1
        if ( rev > (2*-1)**31 and rev < (2**31)-1):
            return rev
        else:
            return 0
    