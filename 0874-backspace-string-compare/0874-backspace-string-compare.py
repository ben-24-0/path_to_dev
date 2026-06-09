class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def bkspc(st):
            stk=[]
            for i in st:
                if(i=="#" ):
                    if(stk):
                        stk.pop()
                else:
                    stk.append(i)

                ns="".join(stk)
            print(ns,end="")
            return ns
        

        return bkspc(s)==bkspc(t)

                
        

                