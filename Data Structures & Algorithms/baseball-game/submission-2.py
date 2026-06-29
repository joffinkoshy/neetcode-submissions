class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        curr_sum=0

        for op in operations:
            if op == "C":
                d=stack.pop()
                curr_sum-=d
            
            elif op == "D":
                curr_sum+=2*stack[-1]
                stack.append(2 * stack[-1])
                

            elif op == "+":
                curr_sum+=(stack[-1]+stack[-2])
                stack.append(stack[-1] + stack[-2])
                

            else:
                stack.append(int(op))
                curr_sum+=int(op)

        return curr_sum