class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}
        stack=[]

        for ch in tokens:
            if ch not in ops:
                stack.append(int(ch))

            else:
                n2=stack.pop()
                n1=stack.pop()

                if ch =='+':
                    stack.append(n1+n2)
                elif ch=='-':
                    stack.append(n1-n2)
                elif ch=='*':
                    stack.append(n1*n2)
                else:
                    stack.append(int(n1/n2))

        return stack[-1]
                
        


        