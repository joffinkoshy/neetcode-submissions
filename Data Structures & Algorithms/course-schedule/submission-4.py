from collections import deque,defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        degree=[0]*numCourses
        q=deque()
        g = [[] for _ in range(numCourses)]

        for a,b in prerequisites:
            degree[a]+=1
            g[b].append(a)

        for i in range(numCourses):
            if degree[i]==0:
                q.append(i)
        

        append=q.append
        popleft=q.popleft

        while q:
            c=popleft()
            numCourses-=1

            for nxt in g[c]:
                degree[nxt]-=1
                if degree[nxt]==0:
                    append(nxt)

        return numCourses==0


        

        
        