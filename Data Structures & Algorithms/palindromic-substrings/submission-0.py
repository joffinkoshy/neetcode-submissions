class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        ans=0

        def expand(left,right):
            count=0
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1 # expand around a center moves left and right

                count+=1

            return count

        
        for i in range(n):
            #Odd-lengthed Palindrome
            ans+=expand(i,i)

            # even length
            ans+=expand(i,i+1)

        return ans
        


        