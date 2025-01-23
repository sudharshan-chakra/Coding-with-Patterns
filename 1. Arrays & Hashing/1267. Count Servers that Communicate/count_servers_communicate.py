'''
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
Return the number of servers that communicate with any other server.

Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
'''

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rowcount, colcount = [0 for _ in range(rows)], [0 for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    rowcount[i] += 1
                    colcount[j] += 1
        
        out = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (rowcount[i] > 1 or colcount[j] > 1):
                    out += 1

        return out 