import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        tails=[]

        for x in nums:
            pos=bisect.bisect_left(tails,x)
            if pos==len(tails):
                tails.append(x)
            else:
                tails[pos]=x

        return len(tails)
        

        