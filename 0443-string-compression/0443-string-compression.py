class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i=0
        j=0
        nw=""
        while(i<len(chars)):
            count=0
            j=i
            while(j<len(chars)):
                if(chars[i]!=chars[j]):
                    break
                j+=1
                count+=1
            if count >1:
                nw = nw + chars[i]+ str(count) 
            else:
                nw = nw + chars[i]
            i+=count
        li = list(nw)
        n = len(li)
        print(n)
        chars[:]= list(nw)
        return len(chars)

                
        