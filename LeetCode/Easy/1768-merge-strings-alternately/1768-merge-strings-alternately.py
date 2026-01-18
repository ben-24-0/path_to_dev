class Solution(object):
    def mergeAlternately(self, word1, word2):
        l=min(len(word1),len(word2))
        w1=list(word1)
        w2=list(word2)
        k=0
        for i in range (1,l+1):
            w1.insert(k+i,w2[i-1])
            k+=1

        w2=w2[l:len(w2)+1]
        print(w2)
        w3 = "".join(w1) + "".join(w2)
        return w3



