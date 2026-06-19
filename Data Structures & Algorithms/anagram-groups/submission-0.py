class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = {}

        for word in strs:
            freq = [0] * 26

            for ch in word:
                freq[ord(ch) - ord('a')] += 1

            key = tuple(freq)

            if key in grouping:
                grouping[key].append(word)
            else:
                grouping[key] = [word]

        return list(grouping.values())