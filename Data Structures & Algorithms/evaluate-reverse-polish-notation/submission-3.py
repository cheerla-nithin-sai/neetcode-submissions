class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        l = ["+","-","*","/"]
        for i in tokens:
            if i not in l:
                s.append(int(i))
            elif i=="*":
                s.append(s.pop()*s.pop())
            elif i=="+":
                s.append(s.pop()+s.pop())
            elif i=="-":
                a,b=s.pop(),s.pop()
                s.append(b-a)
            else:
                a,b=s.pop(),s.pop()
                s.append(int(float(b)/a))
        return s[-1]