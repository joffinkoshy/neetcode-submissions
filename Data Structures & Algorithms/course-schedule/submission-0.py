from collections import deque,defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n=numCourses
        degree=[0]*n
        q=deque()
        g=defaultdict(list)

        for a,b in prerequisites:
            degree[a]+=1
            g[b].append(a)

        for i in range(n):
            if degree[i]==0:
                q.append(i)
        count=0

        while q:
            c=q.popleft()
            count+=1

            for nxt in g[c]:
                degree[nxt]-=1
                if degree[nxt]==0:
                    q.append(nxt)

        return count==n


        

        
        