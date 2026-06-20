class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for ch in s:
            if ch in p:
                stack.append(ch)
            else:
                if not stack or p[stack[-1]] != ch:
                    return False
                stack.pop()

        return len(stack) == 0