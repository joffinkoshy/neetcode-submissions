class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        l=0
        n=len(arr)
        # fixed size sliding window
        curr=0

        for r in range(n):
            curr+=arr[r]

            if r-l+1==k:
                if curr>=threshold*k:
                    count+=1
                curr-=arr[l]
                l+=1

        return count


        