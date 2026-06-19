from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)

        sorted_items=sorted(freq.items(),key=lambda x: x[1],reverse=True)

        ans=[]
        for i in range(k):
            n,f=sorted_items[i]
            ans.append(n)

        return ans

        

        