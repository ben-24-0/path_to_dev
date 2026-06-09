class Solution:
    def simplifyPath(self, path: str) -> str:
        s = (path.split("/"))
        stk=[]
 
        print(s)
        for i in s:
            if(i=="" or i=="."):
                continue
            elif i=="..":
                if stk:
                    stk.pop()
            else:
                 stk.append(i)
            
        return "/"+ "/".join(stk)






        