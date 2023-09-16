# https://leetcode.com/problems/path-with-minimum-effort/description/?envType=daily-question&envId=2023-09-16
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        efforts = [[float('inf') for _ in range(n)] for i in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        efforts[0][0] = 0
 
        stack = [(0, (0, 0))]

        while stack:
            curr = heappop(stack)
            x, y = curr[-1]
            for dx, dy in directions:
                if x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n:
                    curr_effort = abs(heights[x][y] - heights[x+dx][y+dy])
                    # print(x+dx,y+dy)
                    # print(x,y)
                    new_effort = max(efforts[x][y], curr_effort)
                    if efforts[x+dx][y+dy] > new_effort:
                        efforts[x+dx][y+dy] = new_effort
                        heappush(stack, (efforts[x+dx][y+dy], (x+dx,y+dy)))
        return int(efforts[-1][-1])