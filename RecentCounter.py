#https://leetcode.com/problems/number-of-recent-calls/submissions/

class RecentCounter:

    def __init__(self):
        from collections import deque
        self.ping_list = deque() # stores t of the pings

    def ping(self, t: int) -> int:
        self.ping_list.append(t)

        val = self.ping_list[0]
        while (t-val) > 3000:
            self.ping_list.popleft()
            val = self.ping_list[0]

        count = len(self.ping_list)

        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)