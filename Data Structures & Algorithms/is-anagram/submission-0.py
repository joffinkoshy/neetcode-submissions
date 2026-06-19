class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq=[0]*26

        for ch in s:
            idx=ord(ch)-ord('a')
            freq[idx]+=1

        for ch in t:
            idx=ord(ch)-ord('a')
            if freq[idx]==0:
                return False
            freq[idx]-=1

        for f in freq:
            if f!=0:
                return False

        return True

            


        