# Minimum Time Visiting All Points
#
# On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.
#
# You can move according to the next rules:
#
# In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
# You have to visit the points in the same order as they appear in the array.
#
#
# Example 1:
#
#
# Input: points = [[1,1],[3,4],[-1,0]]
# Output: 7
# Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
# Time from [1,1] to [3,4] = 3 seconds
# Time from [3,4] to [-1,0] = 4 seconds
# Total time = 7 seconds
# Example 2:
#
# Input: points = [[3,2],[-2,2]]
# Output: 5
#
#
# Constraints:
#
# points.length == n
# 1 <= n <= 100
# points[i].length == 2
# -1000 <= points[i][0], points[i][1] <= 1000



points = [[1,1],[3,4],[-1,0]]
for index in range(0,len(points)-1):
    steps = 0
    x1 = points[index][0]
    y1 = points[index][1]
    x2 = points[index+1][0]
    y2 = points[index+1][1]
    if x2 != x1 and y2 != y1:
        while x2 != x1 or y2 != y1:
            print(x1)
            if x2 > x1:
                x1 +=1
            else:
                x1-=1
            if y2 > y1:
                y1 +=1
            else:
                y1-=1
            steps +=1
    else:
        while x2 != x1:
            if x2 > x1:
                x1 +=1
            else:
                x1-=1
            steps +=1
        while y2 != y1:
            if y2 > y1:
                y1 +=1
            else:
                y1-=1
            steps +=1
    print(steps)
