from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead=set(deadends)
        q=deque()

        if "0000" in dead:
            return -1

        q.append(('0000',0))
        visited={'0000'}

        while q:
            state,moves=q.popleft()

            if state==target:
                return moves

            for i in range(4):
                digit=int(state[i])

                up=(digit+1)%10
                next_state=state[:i]+str(up)+state[i+1:]
                if next_state not in visited and next_state not in dead:
                    visited.add(next_state)
                    q.append((next_state,moves+1))

                down=(digit-1)%10
                next_state=state[:i]+str(down)+state[i+1:]
                if next_state not in visited and next_state not in dead:
                    visited.add(next_state)
                    q.append((next_state,moves+1))

        return -1

                



        