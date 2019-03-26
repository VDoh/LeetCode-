from typing import List

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        LeftMax = [max(i) for i in grid]
        TopMax = [max(j) for j in zip(*grid)]
        sum = 0

        for k in range(len(grid)):
            for m in range(len(grid[k])):
                sum += min(LeftMax[k],LeftMax[m]) - grid[k][m]
    
        return sum 

        

s = Solution()

sum = s.maxIncreaseKeepingSkyline(grid)

print(sum)