class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        curr_sum = 0

        for op in operations:
            if op == "C":
                score = stack.pop()
                curr_sum -= score

            elif op == "D":
                score = 2 * stack[-1]
                stack.append(score)
                curr_sum += score

            elif op == "+":
                score = stack[-1] + stack[-2]
                stack.append(score)
                curr_sum += score

            else:
                score = int(op)
                stack.append(score)
                curr_sum += score

        return curr_sum