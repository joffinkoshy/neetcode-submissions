from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)

        l = 0
        start = 0
        min_len = float('inf')

        for r in range(len(s)):
            if need[s[r]] > 0:
                missing -= 1

            need[s[r]] -= 1

            while missing == 0:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l

                need[s[l]] += 1

                if need[s[l]] > 0:
                    missing += 1

                l += 1

        return "" if min_len == float('inf') else s[start:start + min_len]