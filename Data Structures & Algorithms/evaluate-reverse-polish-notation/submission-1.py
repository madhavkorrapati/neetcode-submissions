class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res=[]
        for i in tokens:
            if i in "*":
                b=res.pop()
                a=res.pop()
                res.append(a*b)
            elif i in "/":
                b=res.pop()
                a=res.pop()
                res.append(int(a/b))
            elif i in "-":
                b=res.pop()
                a=res.pop()
                res.append(a-b)
            elif i in "+":
                b=res.pop()
                a=res.pop()
                res.append(a+b)
            else:
                res.append(int(i))
        return res[-1]
        

