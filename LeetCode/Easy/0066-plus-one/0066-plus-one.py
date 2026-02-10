class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        st=""
        l=[]
        for i in range(len(digits)):
            st  = st + str(digits[i])
        nd = int(st)+1
        while (nd>0):
            rem = nd%10
            l.append((rem))
            nd = nd//10
        return l[::-1]