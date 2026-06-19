class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)

        if m > n:
            return False

        freq_1 = [0] * 26

        for ch in s1:
            freq_1[ord(ch) - ord('a')] += 1

        for i in range(n - m + 1):
            freq = freq_1[:]

            for r in range(i, i + m):
                idx = ord(s2[r]) - ord('a')

                if freq[idx] == 0:
                    break

                freq[idx] -= 1
            else:  # runs only if loop didn't break
                return True

        return False